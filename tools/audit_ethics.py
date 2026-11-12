#!/usr/bin/env python3
"""Read-only, redacted secret-pattern audit of locally reachable Git history.

Run with Python and pypdf. No network calls or credential validation are made.
This is a bounded pattern search, not a penetration test or a guarantee.
"""
from pathlib import Path
from collections import Counter
from io import BytesIO
import argparse
import hashlib
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RULES = {
    'private-key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----'),
    'aws-access-id': re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    'github-token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b'),
    'provider-token': re.compile(r'\b(?:sk-(?:proj-)?[A-Za-z0-9_-]{20,}|xox[baprs]-[A-Za-z0-9-]{15,})\b'),
    'jwt-literal': re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b'),
    'url-credential': re.compile(r'\b[a-z][a-z0-9+.-]*://[^\s:/<>"\']{1,80}:[^\s/@<>"\']{1,120}@', re.I),
    'credential-assignment': re.compile(r'''(?ix)["']?\b(?:password|passwd|api[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|secret[_-]?key)\b["']?\s*[:=]\s*["']([^"'\r\n]{1,256})["']'''),
}
PLACEHOLDERS = {'example', '<token>', 'text', '<secret>', 'placeholder'}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def run_audit():
    findings, placeholders, unsupported, errors = [], [], [], []
    counts = Counter()

    def scan(data, origin, depth=0):
        counts['payloads'] += 1
        if data.startswith(b'%PDF-'):
            from pypdf import PdfReader
            try:
                reader = PdfReader(BytesIO(data))
                text = '\n'.join(p.extract_text() or '' for p in reader.pages)
                counts['pdf_text_extractions'] += 1
            except Exception as exc:
                errors.append({'origin': origin, 'error': type(exc).__name__})
                return
        elif data.startswith(b'PK\x03\x04'):
            if depth >= 2:
                unsupported.append(origin + ': nested archive limit')
                return
            with zipfile.ZipFile(BytesIO(data)) as archive:
                for info in archive.infolist():
                    if info.is_dir():
                        continue
                    if info.file_size > 16_777_216:
                        unsupported.append(origin + ':' + info.filename + ': size limit')
                    else:
                        scan(archive.read(info), origin + ':' + info.filename, depth + 1)
            return
        elif b'\0' in data[:8192]:
            unsupported.append(origin + ': binary (no OCR or binary decoding)')
            return
        else:
            text = data.decode('utf-8', errors='replace')
            counts['text_payloads'] += 1
        for rule, pattern in RULES.items():
            for match in pattern.finditer(text):
                record = {'origin': origin, 'line': text.count('\n', 0, match.start()) + 1, 'rule': rule}
                if rule == 'credential-assignment' and match.group(1).lower() in PLACEHOLDERS:
                    placeholders.append(record)
                else:
                    findings.append(record)

    objects = git('rev-list', '--objects', '--all', '--reflog').decode().splitlines()
    seen = set()
    for row in objects:
        oid, _, path = row.partition(' ')
        if oid in seen:
            continue
        seen.add(oid)
        if git('cat-file', '-t', oid).strip() == b'blob':
            counts['unique_history_blobs'] += 1
            scan(git('cat-file', 'blob', oid), 'git:' + oid[:12] + ':' + path)
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if any(p in {'.git', '__pycache__', '.venv', 'node_modules', 'tmp'} for p in rel.parts):
            continue
        if path.is_file():
            counts['worktree_files'] += 1
            scan(path.read_bytes(), 'worktree:' + str(rel))
    return {
        'audit_date': '2026-11-11',
        'base_head': git('rev-parse', 'HEAD').decode().strip(),
        'reachable_commits': int(git('rev-list', '--all', '--reflog', '--count')),
        'refs': git('for-each-ref', '--format=%(refname) %(objectname)').decode().splitlines(),
        'rules': list(RULES),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'counts': dict(counts),
        'unresolved_candidates': findings,
        'documented_placeholder_matches': placeholders,
        'unsupported_payloads': unsupported,
        'extraction_errors': errors,
        'limits': 'Local refs/reflogs only; remote not fetched; no unreachable objects, external prototypes, OCR, runtime/config inspection, entropy scan, or credential validity checks. Binary exclusions listed. Match values are never printed.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = run_audit()
    result = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end='')
    raise SystemExit(bool(report['unresolved_candidates'] or report['extraction_errors']))
