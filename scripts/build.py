"""Render the explicitly selected research documents through GitHub's GFM API."""

import concurrent.futures
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess

from presentation import comparison_notes, contents, directory, image_viewer
from media import posters, previews

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SITE = ROOT / "site"
CACHE = ROOT / ".render-cache"
BASE_URL = "https://mine2424.github.io/oprol-qa-research/"
NAV = [
    ("index.html", "製品一覧"),
    ("competitor-evidence/2026-10-27/gallery.html", "画像と動画"),
    ("02-competitors.html", "市場と価格"),
]


def relative(target, page):
    return os.path.relpath(SITE / target, page.parent)


def navigation(page):
    links = []
    for target, label in NAV:
        selected = SITE / target == page or (target == "index.html" and page.parent.name == "competitor-products")
        current = ' aria-current="page"' if selected else ""
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
    is_gallery = page.name == "gallery.html"
    is_directory = page in (SITE / "index.html", SITE / "competitor-products/README.html")
    body, toc = (body, "") if is_gallery or is_directory else contents(body)
    product = page.parent.name == "competitor-products" and page.name != "README.html"
    breadcrumb = f'<p class="breadcrumb"><a href="{relative("index.html", page)}">製品一覧</a><span aria-hidden="true"> / </span>{html.escape(title.split(" — ")[0])}</p>' if product else ""
    page_class = "page-gallery" if is_gallery else "page-document"
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
<link rel="stylesheet" href="{relative('styles.css', page)}?v=5">
<link rel="stylesheet" href="{relative('research.css', page)}?v=5">
</head><body><a class="skip" href="#content">本文へ移動</a>
<header class="site-header"><div class="header-inner"><div class="header-top"><a class="brand" href="{relative('index.html', page)}">Oprol QA <span>Research</span></a><span class="edition">競合調査 / 2026.10.27</span></div>{navigation(page)}</div></header>
<div class="page-layout {page_class}{' with-toc' if toc else ''}"><main id="content" tabindex="-1">{breadcrumb}{body}</main>{toc}</div>
<footer><p><a href="{relative('competitor-flows.html', page)}">比較の見どころ</a> · <a href="{relative('competitor-inventory.html', page)}">調査対象について</a> · <a href="{relative('competitor-evidence/2026-10-27/README.html', page)}">画像・動画の出典と確認方法</a></p><p>2026年10月27日版 · 各社の画面・映像の権利は各権利者に帰属します。</p></footer>
{image_viewer()}<script src="{relative('site.js', page)}?v=5" defer></script></body></html>'''


def build_document(source, poster_paths):
    target = SITE / source.relative_to(CONTENT).with_suffix(".html")
    target.parent.mkdir(parents=True, exist_ok=True)
    text = source.read_text()
    title = text.splitlines()[0].removeprefix("# ")
    body = render_markdown(text)
    body = re.sub(r'(href|src)="([^"]+)"', rewrite_link, body)
    body = body.replace('<img ', '<img loading="lazy" ')
    body = re.sub(r'<table(?: [^>]*)?>(.*?)</table>', r'<div class="table-scroll" role="region" aria-label="比較表。横にスクロールできます" tabindex="0"><table>\1</table></div>', body, flags=re.S)
    if target.name == "competitor-flows.html":
        body = comparison_notes(body)
        title = "比較の見どころ"
    if target in (SITE / "index.html", SITE / "competitor-products/README.html"):
        title = "AI QA・テスト支援ツール比較"
        body = directory(poster_paths, target)
    elif target.parent.name == "competitor-products":
        body = previews(body, target, poster_paths)
    body = body.replace(">全体比較</a>", ">比較の見どころ</a>")
    target.write_text(wrap(title, body, target))
    print(target.relative_to(SITE), flush=True)


def build_gallery(poster_paths):
    path = SITE / "competitor-evidence/2026-10-27/gallery.html"
    content = (CONTENT / "competitor-evidence/2026-10-27/gallery.html").read_text()
    body = re.search(r'</style>(.*)<script>', content, re.S).group(1)
    body = body.replace('<header>', '<div class="gallery-tools">').replace('</header>', '</div>')
    body = body.replace('<main>', '<div class="gallery-content">').replace('</main>', '</div>')
    body = body.replace('<nav class="index">', '<nav class="index" aria-label="製品別ショートカット">')
    body = body.replace('<nav class="index"', '<details class="product-picker"><summary>製品名から移動（40件）</summary><nav class="index"', 1)
    body = body.replace('</nav>', '</nav></details>', 1)
    body = re.sub(r'<details(?: open)? class="image-label">', '<details open class="image-label">', body)
    body = body.replace('<input id="query"', '<label for="query">製品・機能を検索</label><input id="query"')
    body = body.replace('<select id="mode"', '<label for="mode">表示するメディア</label><select id="mode"')
    body = body.replace('<span id="count">', '<span id="count" role="status" aria-live="polite">')
    body = body.replace('<video ', '<video playsinline ')
    def video(match):
        source = (path.parent / match[1]).resolve()
        poster = os.path.relpath(poster_paths[source], path.parent)
        return match[0].replace('<video ', f'<video poster="{poster}" ')
    body = re.sub(r'<video[^>]+src="([^"]+)"', video, body)
    body = body.replace('<input id="query"', '<input type="search" id="query"')
    body = body.replace('<span id="count"', '<button type="button" id="gallery-reset">検索をクリア</button><span id="count"')
    body = re.sub(r'(href|src)="([^"]+)"', rewrite_link, body)
    body += f'<script src="{relative("gallery.js", path)}?v=5" defer></script>'
    body = body.replace(">全体の比較表</a>", ">比較の見どころ</a>")
    path.write_text(wrap("競合プロダクトの機能・画面・動画", body, path))


if __name__ == "__main__":
    CACHE.mkdir(exist_ok=True)
    poster_paths = posters()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(lambda source: build_document(source, poster_paths), sorted(CONTENT.rglob("*.md"))))
    build_gallery(poster_paths)
