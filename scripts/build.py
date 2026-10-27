"""Render the explicitly selected research documents through GitHub's GFM API."""

import concurrent.futures
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SITE = ROOT / "site"
CACHE = ROOT / ".render-cache"
BASE_URL = "https://mine2424.github.io/oprol-qa-research/"
NAV = [
    ("index.html", "概要"),
    ("competitor-flows.html", "機能・導線比較"),
    ("competitor-products/README.html", "製品別詳細"),
    ("competitor-evidence/2026-10-27/gallery.html", "画像・動画"),
    ("02-competitors.html", "市場・価格比較"),
    ("competitor-inventory.html", "候補台帳"),
]


def relative(target, page):
    return os.path.relpath(SITE / target, page.parent)


def navigation(page):
    links = []
    for target, label in NAV:
        current = ' aria-current="page"' if SITE / target == page else ""
        links.append(f'<a href="{relative(target, page)}"{current}>{label}</a>')
    return '<nav aria-label="資料ナビゲーション">' + "".join(links) + "</nav>"


def rewrite_link(match):
    attribute, url = match.groups()
    if not url.startswith(("https:", "http:", "#", "mailto:")):
        url = re.sub(r"\.md(?=#|$)", ".html", url)
    return f'{attribute}="{url}"'


def render_markdown(source):
    digest = hashlib.sha256(source.encode()).hexdigest()
    cached = CACHE / (digest + ".html")
    if cached.exists():
        return cached.read_text()
    result = subprocess.run(
        ["gh", "api", "markdown", "--method", "POST", "--input", "-"],
        input=json.dumps({"text": source, "mode": "gfm"}),
        text=True, capture_output=True, check=True,
    )
    cached.write_text(result.stdout)
    return result.stdout


def wrap(title, body, page):
    description = "AI QA・テスト支援40製品／サービスの機能・導線・画面・動画を整理した調査資料。確認日と未確認範囲を明記。"
    canonical = BASE_URL + str(page.relative_to(SITE))
    return f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | Oprol QA Research</title>
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ja_JP">
<meta property="og:title" content="{html.escape(title)} | Oprol QA Research">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}social.png">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{relative('favicon.svg', page)}" type="image/svg+xml">
<link rel="stylesheet" href="{relative('styles.css', page)}">
</head><body><a class="skip" href="#content">本文へ移動</a>
<header class="site-header"><a class="brand" href="{relative('index.html', page)}">Oprol QA <span>Research</span></a>{navigation(page)}</header>
<main id="content" tabindex="-1">{body}</main>
<footer>調査資料 · 2026年10月27日版 · 各社の画面・映像の権利は各権利者に帰属します。出典と確認範囲は各ページをご覧ください。</footer>
<script src="{relative('site.js', page)}" defer></script></body></html>'''


def build_document(source):
    target = SITE / source.relative_to(CONTENT).with_suffix(".html")
    target.parent.mkdir(parents=True, exist_ok=True)
    text = source.read_text()
    title = text.splitlines()[0].removeprefix("# ")
    body = render_markdown(text)
    body = re.sub(r'(href|src)="([^"]+)"', rewrite_link, body)
    body = body.replace('<img ', '<img loading="lazy" ')
    body = re.sub(r'<table(?: [^>]*)?>(.*?)</table>', r'<div class="table-scroll" role="region" aria-label="比較表。横にスクロールできます" tabindex="0"><table>\1</table></div>', body, flags=re.S)
    target.write_text(wrap(title, body, target))
    print(target.relative_to(SITE), flush=True)


def build_gallery():
    path = SITE / "competitor-evidence/2026-10-27/gallery.html"
    content = (CONTENT / "competitor-evidence/2026-10-27/gallery.html").read_text()
    body = re.search(r'</style>(.*)<script>', content, re.S).group(1)
    body = body.replace('<header>', '<div class="gallery-tools">').replace('</header>', '</div>')
    body = body.replace('<main>', '<div class="gallery-content">').replace('</main>', '</div>')
    body = body.replace('<nav class="index">', '<nav class="index" aria-label="製品別ショートカット">')
    body = body.replace('<input id="query"', '<label for="query">製品・機能を検索</label><input id="query"')
    body = body.replace('<select id="mode"', '<label for="mode">表示するメディア</label><select id="mode"')
    body = body.replace('<span id="count">', '<span id="count" role="status" aria-live="polite">')
    body = body.replace('<video ', '<video playsinline ')
    body = re.sub(r'(href|src)="([^"]+)"', rewrite_link, body)
    script = re.search(r'<script>(.*)</script>', content, re.S).group(1)
    # Do not carry an inline script into the generated document.
    (SITE / "gallery.js").write_text(script)
    body += f'<script src="{relative("gallery.js", path)}" defer></script>'
    path.write_text(wrap("競合プロダクトの機能・画面・動画", body, path))


if __name__ == "__main__":
    CACHE.mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(build_document, sorted(CONTENT.rglob("*.md"))))
    build_gallery()
