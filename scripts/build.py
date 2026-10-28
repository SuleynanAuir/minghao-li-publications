"""Generate a buildless GitHub Pages PDF library using only Python's stdlib."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parent.parent
publications = json.loads((ROOT / 'publications.json').read_text())
assert len({item['id'] for item in publications}) == len(publications)
reader_dir = ROOT / 'readers'
reader_dir.mkdir(exist_ok=True)
cards = []
for item in publications:
    pdf = ROOT / item['pdf']
    title = item['title']
    slug = item['id']
    web_copy = ROOT / 'output/pdf' / pdf.relative_to(ROOT / 'additional-backup')
    served_pdf = web_copy if web_copy.is_file() else pdf
    if served_pdf.stat().st_size >= 100 * 1024 * 1024:
        raise ValueError(f'PDF exceeds GitHub file limit; prepare a web copy: {pdf}')
    url = '../' + quote(served_pdf.relative_to(ROOT).as_posix(), safe='/')
    safe_title = escape(title)
    page = f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{safe_title} · Minghao Li | Publications</title>
  <style>
    html,body{{margin:0;width:100%;height:100%;background:#292b30}}
    iframe{{display:block;width:100%;height:100%;height:100dvh;border:0}}
    details{{position:fixed;right:16px;bottom:16px;max-width:calc(100vw - 64px);padding:10px 14px;background:#fff;color:#26304a;border-radius:8px;font:14px/1.6 system-ui;box-shadow:0 2px 16px #0003}}
    summary{{cursor:pointer}}a{{color:#245baf}}p{{margin:8px 0 0}}
  </style>
</head>
<body>
  <iframe src="{url}#view=FitH" title="{safe_title} — PDF 在线阅读"></iframe>
  <details><summary>无法显示？</summary><p><a href="{url}" target="_blank" rel="noopener">在新标签页打开 PDF</a></p><p>若浏览器禁用了 PDF 预览，请开启预览或换用支持 PDF 的浏览器。</p><p><a href="../index.html">返回文档目录</a></p></details>
</body>
</html>
'''
    destination = ROOT / slug
    destination.mkdir(exist_ok=True)
    (destination / 'index.html').write_text(page, encoding='utf-8')
    target = '../' + slug + '/'
    redirect = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={target}"><title>{safe_title}</title></head><body><a href="{target}">打开阅读页：{safe_title}</a></body></html>'''
    (reader_dir / item['legacy']).write_text(redirect, encoding='utf-8')
    category = '演示文档' if 'demo' in pdf.relative_to(ROOT / 'additional-backup').parts[:-1] else '研究文档'
    size = served_pdf.stat().st_size / 1024 / 1024
    cards.append(f'<li><a href="{slug}/"><span class="meta">{category} · PDF · {size:.1f} MB</span><h2>{safe_title}</h2><span class="read">在线阅读 <span aria-hidden="true">↗</span></span></a></li>')

index = '''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Minghao Li | Publications：研究与演示文档，直接在线阅读。">
  <title>Minghao Li | Publications</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <header><p class="eyebrow">PUBLICATIONS &amp; RESEARCH</p><h1>Minghao Li<span>.</span></h1><p class="intro">Minghao Li 的论文与研究文档，支持在线阅读。</p></header>
    <section aria-label="文档目录">
      <div class="toolbar"><p>文档目录 <span id="count">COUNT 份</span></p><label><span class="sr-only">搜索文档标题</span><input id="search" type="search" placeholder="搜索文档标题…" autocomplete="off"></label></div>
      <ul id="documents">CARDS</ul>
      <p id="empty" hidden>没有找到匹配的文档，请尝试其他关键词。</p>
      <p id="status" class="sr-only" role="status" aria-live="polite"></p>
    </section>
    <footer>MINGHAO LI <span>在线文档库</span></footer>
  </main>
  <script src="search.js"></script>
</body>
</html>
'''.replace('COUNT', str(len(publications))).replace('CARDS', '\n'.join(cards))
(ROOT / 'index.html').write_text(index, encoding='utf-8')
print(f'Generated index and {len(publications)} reading pages.')

base = 'https://suleynanauir.github.io/minghao-li-publications/'
section = ['## Read Online', '', f'[Browse the Library]({base}) · [GitHub Repository](https://github.com/SuleynanAuir/minghao-li-publications)', '', 'Each link opens a dedicated full-page PDF reader. Previously shared long reader URLs redirect to the corresponding short URL. Plain-text link list: [paper-links.txt](paper-links.txt).', '']
plain = ['Minghao Li | Publications', base, '']
number = 0
for category, label in [('research', 'Research Papers and Documents'), ('demo', 'Presentations and Reports')]:
    section += ['### ' + label, '', '| No. | Document | Read Online |', '| --- | --- | --- |']
    plain += [label, '']
    for item in publications:
        if item['category'] != category:
            continue
        number += 1
        link = base + item['id'] + '/'
        section.append(f"| {number} | {item['title']} | [{item['id']}]({link}) |")
        plain += [f"{number:02d}. {item['title']}", link, '']
    section += ['']
readme = ROOT / 'README.md'
text = readme.read_text()
start = text.index('## Read Online')
end = text.index('## How the Library Works', start)
readme.write_text(text[:start] + '\n'.join(section) + '\n' + text[end:])
(ROOT / 'paper-links.txt').write_text('\n'.join(plain))
