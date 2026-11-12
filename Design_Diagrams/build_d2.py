#!/usr/bin/env python3
"""Compile matching LaTeX reports and build the consolidated PDF.

Requires pypdf and Tectonic (--engine /path/to/tectonic). D2 figures are
embedded in D2_Detailed_Design.tex. User_Stories_Formatted.tex is the editable
LaTeX companion used in the combined report. Every section is compiled from LaTeX for the combined copy. Standalone D0/D1
and original User_Stories files are preserved. Update D2 Section 6 and Peer_Review_Notes.md together.
"""
from pathlib import Path
import argparse, hashlib, os, re, shutil, subprocess, tempfile
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parent

def compile_report(engine, cache, only_cached, name, output_dir):
    if not engine:
        raise SystemExit('Install Tectonic or pass --engine /path/to/tectonic.')
    cmd = [engine, '--untrusted', '--keep-logs', '--outdir', str(output_dir)]
    if only_cached:
        cmd.append('--only-cached')
    cmd.append(name + '.tex')
    env = dict(os.environ)
    if cache:
        env['TECTONIC_CACHE_DIR'] = str(Path(cache).resolve())
    proc = subprocess.run(cmd, cwd=ROOT, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode:
        raise SystemExit(proc.stdout[-10000:])
    log = (output_dir / (name + '.log')).read_text(errors='replace')
    warnings = [s for s in log.splitlines() if 'Overfull' in s or 'Missing character' in s]
    if warnings:
        raise SystemExit(name + ': fix layout before packaging:\n' + '\n'.join(warnings))
    return output_dir / (name + '.pdf')

def merge(stories_pdf, d0_pdf, d1_pdf, d2_pdf):
    sources = [
        ('User stories and use cases', stories_pdf),
        ('Design D0', d0_pdf),
        ('Design D1', d1_pdf),
        ('Design D2', d2_pdf),
    ]
    writer = PdfWriter()
    offset = 0
    review_page = None
    for title, path in sources:
        reader = PdfReader(path)
        writer.append(reader, import_outline=False)
        writer.add_outline_item(title, offset)
        if title == 'Design D2':
            for i, page in enumerate(reader.pages):
                if '6 Peer design review notes' in ' '.join((page.extract_text() or '').split()):
                    review_page = offset + i
        print(f'{title}: pages {offset + 1}-{offset + len(reader.pages)}')
        offset += len(reader.pages)
    if review_page is None:
        raise SystemExit('Peer review section must be present at the end of D2.')
    writer.add_outline_item('Peer design review notes', review_page)
    writer.add_metadata({
        '/Title': 'In-Home Assistive Robot: User Stories and Design Diagrams',
        '/Author': 'Gavin Lamphier; Liam Patel; Austin Heiss',
        '/Subject': 'Consolidated LaTeX design; peer review recorded, follow-up validation pending',
        '/D2SourceSHA256': hashlib.sha256((ROOT / 'D2_Detailed_Design.tex').read_bytes()).hexdigest(),
        '/UserStoriesLaTeXSHA256': hashlib.sha256((ROOT / 'User_Stories_Formatted.tex').read_bytes()).hexdigest(),
    })
    output = ROOT / 'Design_Diagrams_Consolidated.pdf'
    with output.open('wb') as stream:
        writer.write(stream)
    final = PdfReader(output)
    expected = [p.extract_text() for _, path in sources for p in PdfReader(path).pages]
    if expected != [p.extract_text() for p in final.pages]:
        raise SystemExit('Merged text/order verification failed.')
    shutil.copyfile(d2_pdf, ROOT / 'D2_Detailed_Design.pdf')
    print(f'Combined {len(final.pages)} pages. Peer notes start on page {review_page + 1}.')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--engine', default=shutil.which('tectonic'))
    ap.add_argument('--cache-dir')
    ap.add_argument('--only-cached', action='store_true')
    args = ap.parse_args()
    source = (ROOT / 'User_Stories_Formatted.tex').read_text()
    recorded = re.search(r'^% Source Markdown SHA256: ([0-9a-f]{64})$', source, re.M)
    current = hashlib.sha256((ROOT.parent / 'User_Stories.md').read_bytes()).hexdigest()
    if recorded and recorded.group(1) != current:
        raise SystemExit('User_Stories.md changed: reconcile the LaTeX companion before building.')
    with tempfile.TemporaryDirectory(prefix='robot-design-latex-') as tmp:
        temp = Path(tmp)
        stories = compile_report(args.engine, args.cache_dir, args.only_cached, 'User_Stories_Formatted', temp)
        d0 = compile_report(args.engine, args.cache_dir, args.only_cached, 'D0_High_Level_Design', temp)
        d1 = compile_report(args.engine, args.cache_dir, args.only_cached, 'D1_Detailed_Design', temp)
        d2 = compile_report(args.engine, args.cache_dir, args.only_cached, 'D2_Detailed_Design', temp)
        merge(stories, d0, d1, d2)
