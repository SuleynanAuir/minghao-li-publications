"""Generate a buildless GitHub Pages PDF library using only Python's stdlib."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import hashlib
import re

ROOT = Path(__file__).resolve().parent.parent
pdfs = sorted(set((ROOT / 'additional-backup').rglob('*.pdf')) | {ROOT / 'additional-backup' / p.relative_to(ROOT / 'output/pdf') for p in (ROOT / 'output/pdf').rglob('*.pdf')})
reader_dir = ROOT / 'readers'
reader_dir.mkdir(exist_ok=True)
cards = []
for pdf in pdfs:
    relative = pdf.relative_to(ROOT).as_posix()
    title = re.sub(r'\s+', ' ', pdf.stem.replace('_', ' ')).strip()
    slug = re.sub(r'[^a-z0-9]+', '-', pdf.stem.lower()).strip('-')
    suffix = hashlib.sha256(relative.encode()).hexdigest()[:8]
    name = f'{slug}-{suffix}.html'
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
    (reader_dir / name).write_text(page, encoding='utf-8')
    category = '演示文档' if 'demo' in pdf.relative_to(ROOT / 'additional-backup').parts[:-1] else '研究文档'
    size = served_pdf.stat().st_size / 1024 / 1024
    cards.append(f'<li><a href="readers/{name}"><span class="meta">{category} · PDF · {size:.1f} MB</span><h2>{safe_title}</h2><span class="read">在线阅读 <span aria-hidden="true">↗</span></span></a></li>')

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
'''.replace('COUNT', str(len(pdfs))).replace('CARDS', '\n'.join(cards))
(ROOT / 'index.html').write_text(index, encoding='utf-8')
print(f'Generated index and {len(pdfs)} reading pages.')
