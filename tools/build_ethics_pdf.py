#!/usr/bin/env python3
"""Build portrait, Times New Roman ethics and companion PDFs from Markdown.

Dependencies: tools/requirements-ethics.txt. Uses installed fonts; no font files
are copied into the repository. Regenerates the exact attribution list in NOTICE.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import argparse
import hashlib
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'Ethics_Statement.md'
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
FONT_FILES = ['Times New Roman.ttf', 'Times New Roman Bold.ttf',
              'Times New Roman Italic.ttf', 'Times New Roman Bold Italic.ttf']
if not (FONT_DIR / FONT_FILES[0]).exists():
    # Metric-compatible fallback (OFL-1.1) for Linux hosts without Times New Roman.
    FONT_DIR = next(p for p in [Path('/usr/share/fonts/truetype/liberation2'),
                                Path('/usr/share/fonts/truetype/liberation')]
                    if (p / 'LiberationSerif-Regular.ttf').exists())
    FONT_FILES = ['LiberationSerif-Regular.ttf', 'LiberationSerif-Bold.ttf',
                  'LiberationSerif-Italic.ttf', 'LiberationSerif-BoldItalic.ttf']
for name, file in zip(['TNR', 'TNR-Bold', 'TNR-Italic', 'TNR-BoldItalic'], FONT_FILES):
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
pdfmetrics.registerFontFamily('TNR', normal='TNR', bold='TNR-Bold', italic='TNR-Italic', boldItalic='TNR-BoldItalic')

BODY = ParagraphStyle('Body', fontName='TNR', fontSize=10, leading=11.3,
                      spaceAfter=5, alignment=TA_LEFT, splitLongWords=True)
TITLE = ParagraphStyle('Title', parent=BODY, fontName='TNR-Bold', fontSize=18,
                       leading=20, spaceAfter=7, keepWithNext=True)
HEADING = ParagraphStyle('Heading', parent=BODY, fontName='TNR-Bold', fontSize=13,
                         leading=15, spaceBefore=5, spaceAfter=7, keepWithNext=True)
CELL = ParagraphStyle('Cell', parent=BODY, fontSize=8.8, leading=9.6, spaceAfter=0)
BULLET = ParagraphStyle('Bullet', parent=BODY, leftIndent=7, firstLineIndent=-7,
                        fontSize=9.6, leading=10.7, spaceAfter=4)
QUOTE = ParagraphStyle('Quote', parent=BODY, fontName='TNR-Italic', leftIndent=10,
                       rightIndent=10, spaceAfter=6)


def inline(value):
    # Parse tokens before XML escaping; hyperlinks never become literal markup.
    pattern = r'(\[[^\]]+\]\([^\s)]+\)|\*\*[^*]+\*\*|`[^`]+`)'
    result = []
    for part in re.split(pattern, value):
        if part.startswith('[') and '](' in part:
            label, url = part[1:-1].split('](', 1)
            result.append('<link href="' + escape(url, {'"': '&quot;'}) + '" color="#243b53">' + escape(label) + '</link>')
        elif part.startswith('**') and part.endswith('**'):
            result.append('<b>' + escape(part[2:-2]) + '</b>')
        elif part.startswith('`') and part.endswith('`'):
            result.append(escape(part[1:-1]))
        else:
            result.append(escape(part))
    return ''.join(result)


def make_table(rows, width, cell_style=CELL):
    n = len(rows[0])
    weights = {8: [.03, .19, .1, .13, .11, .14, .12, .18],
               7: [.25, .105, .145, .08, .065, .105, .25],
               5: [.205, .095, .215, .125, .36],
               4: [.25, .15, .34, .26],
               2: [.34, .66]}[n]
    # The privacy table balances long field lists against explicit retention.
    if n == 7:
        weights = [.33, .07, .12, .075, .085, .085, .235]
        weights = [w / sum(weights) for w in weights]
    if n == 5 and rows[0][0] == 'Tool':
        weights = [.16, .15, .25, .15, .29]
    if n == 4 and rows[0][0] == 'Layer':
        weights = [.13, .28, .22, .37]
    data = [[Paragraph(inline(x), cell_style) for x in row] for row in rows]
    table = Table(data, colWidths=[width * w for w in weights], repeatRows=1,
                  hAlign='LEFT', splitByRow=True)
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 1.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#edf0f2')),
        ('LINEABOVE', (0, 0), (-1, 0), .7, colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), .4, colors.black),
        ('LINEBELOW', (0, 1), (-1, -1), .15, colors.HexColor('#b8bec3')),
        ('LINEBELOW', (0, -1), (-1, -1), .7, colors.black),
    ]))
    return table


def parse_markdown(source, width, styles=None):
    styles = styles or {}
    body = styles.get('body', BODY)
    cell = styles.get('cell', CELL)
    bullet = styles.get('bullet', BULLET)
    quote = styles.get('quote', QUOTE)
    title = styles.get('title', TITLE)
    subtitle = styles.get('subtitle', body)
    lines = source.splitlines()
    output, i = [], 0
    after_title = False
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line == '<!-- pagebreak -->':
            output.append(PageBreak())
            i += 1
        elif line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = [x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', x) for x in row):
                    rows.append(row)
                i += 1
            output.append(make_table(rows, width, cell))
            next_line = next((s.strip() for s in lines[i:] if s.strip()), '')
            if next_line != '<!-- pagebreak -->':
                output.append(Spacer(1, 6))
        elif line.startswith('# '):
            output.append(Paragraph(inline(line[2:]), title))
            i += 1
            after_title = True
        elif line.startswith('## '):
            output.append(Paragraph(inline(line[3:]), HEADING))
            i += 1
        elif line.startswith('- '):
            output.append(Paragraph('- ' + inline(line[2:]), bullet))
            i += 1
        elif line.startswith('> '):
            output.append(Paragraph(inline(line[2:]), quote))
            i += 1
        else:
            parts = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(('|', '#', '<!--', '- ', '> ')):
                parts.append(lines[i].strip())
                i += 1
            output.append(Paragraph('<br/>'.join(inline(x) for x in parts), subtitle if after_title else body))
            after_title = False
    return output


def decorate(canvas, doc):
    canvas.saveState()
    canvas.setFont('TNR', 8)
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawString(doc.leftMargin, 23, doc.footer_label)
    canvas.drawRightString(612 - doc.rightMargin, 23, str(doc.page))
    canvas.restoreState()


def render_document(source_path, title, footer):
    source = source_path.read_text()
    output = source_path.with_suffix('.pdf')
    digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
    doc = SimpleDocTemplate(str(output), pagesize=(612, 792), leftMargin=43,
                            rightMargin=43, topMargin=35, bottomMargin=37,
                            title='In-Home Assistive Robot: ' + title,
                            author='Gavin Lamphier; Liam Patel; Austin Heiss',
                            subject='Owner review/signatures pending; Markdown SHA256 ' + digest)
    doc.footer_label = 'In-Home Assistive Robot | ' + footer
    styles = None
    if source_path == SOURCE:
        styles = {
            'body': ParagraphStyle('EthicsBody', parent=BODY, fontSize=11, leading=12.6, spaceAfter=5),
            'cell': ParagraphStyle('EthicsCell', parent=CELL, fontSize=9.5, leading=10.8),
            'bullet': ParagraphStyle('EthicsBullet', parent=BULLET, fontSize=10.4, leading=12.1, spaceAfter=6),
            'quote': ParagraphStyle('EthicsQuote', parent=QUOTE, fontSize=10.8, leading=13.2),
            'title': ParagraphStyle('EthicsTitle', parent=TITLE, alignment=TA_CENTER),
            'subtitle': ParagraphStyle('EthicsSubtitle', parent=BODY, fontSize=11, leading=12.6, spaceAfter=8, alignment=TA_CENTER),
        }
    doc.build(parse_markdown(source, doc.width, styles), onFirstPage=decorate, onLaterPages=decorate)
    from pypdf import PdfReader
    reader = PdfReader(output)
    print(f'{output}: {len(reader.pages)} pages; source SHA256 {digest}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ethics-only', action='store_true', help='Rebuild only the ethics statement and NOTICE.')
    args = parser.parse_args()
    source = SOURCE.read_text()
    attribution = source.split('## Attribution list\n', 1)[1].split('## AI-use disclosure', 1)[0]
    attribution = re.sub(r'^This exact list is also kept in \[NOTICE.md\]\(NOTICE.md\)[^\n]*\n?', '', attribution, flags=re.M)
    notice = '# Attribution and upstream sources\n\n' + attribution.strip() + '\n\n'
    notice += 'Team-owned source code is MIT licensed; see LICENSE. This attribution inventory does not replace upstream license/NOTICE texts required when dependencies are distributed. See Ethics_Statement.md for versions, obligations and unresolved rights.\n'
    (ROOT / 'NOTICE.md').write_text(notice)
    render_document(SOURCE, 'Ethics Statement', 'Ethics Statement')
    if args.ethics_only:
        return
    for filename, title in [('Constraints_Essay.md', 'Design Constraints and ABET Concerns'),
                             ('Week_09_Schema_and_Stack.md', 'Week 9 Schema and Technology Stack')]:
        path = ROOT / filename
        if path.exists():
            render_document(path, title, title + ' | Owner review pending')


if __name__ == '__main__':
    main()
