"""Presentation helpers; research claims remain in the source documents."""

import html
import os
from pathlib import Path
import re

from media import directory_previews

CONTENT = Path(__file__).resolve().parents[1] / "content"


def contents(body):
    entries = []

    def heading(match):
        number = len(entries) + 1
        label = re.sub(r"<[^>]+>", "", match[1])
        entries.append(f'<a href="#section-{number}">{label}</a>')
        return f'<h2 id="section-{number}">{match[1]}</h2>'

    body = re.sub(r"<h2>(.*?)</h2>", heading, body, flags=re.S)
    if not entries:
        return body, ""
    links = "".join(entries)
    toc = f'<aside class="page-toc"><details open><summary>このページの目次</summary><nav aria-label="このページの目次">{links}</nav></details></aside>'
    return body, toc


def directory(poster_paths, page):
    rows = []
    for line in (CONTENT / "competitor-flows.md").read_text().splitlines():
        if not line.startswith("| ["):
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        found = re.match(r"\[(.+)\]\(competitor-products/(.+)\.md\)", cells[0])
        if not found:
            continue
        name, slug = found.groups()
        text = (CONTENT / f"competitor-products/{slug}.md").read_text()
        scope = text.split("## 調査範囲\n", 1)[1].strip().split("\n", 1)[0]
        site = CONTENT.parent / "site"
        detail = os.path.relpath(site / f"competitor-products/{slug}.html", page.parent)
        gallery = os.path.relpath(site / "competitor-evidence/2026-10-27/gallery.html", page.parent)
        media = directory_previews(text, page, poster_paths)
        rows.append(f'''<li class="directory-card" data-filter-item>
<h2><a href="{detail}">{html.escape(name)}</a></h2>
<p class="directory-scope">{html.escape(scope)}</p>
{media}
<p class="media-count">{html.escape(cells[-2])}</p>
<div class="directory-links"><a href="{detail}" aria-label="{html.escape(name)}を詳しく見る">詳しく見る</a><a href="{gallery}#{slug}" aria-label="{html.escape(name)}の全ての画像と動画">全ての画像と動画</a></div></li>''')
    return f'''<h1>AI QA・テスト支援ツール比較</h1>
<p class="page-intro">40製品の機能・画面・動画をまとめています。製品名や気になる機能から探せます。</p>
<div data-filter-root><div class="filter-bar"><div><label for="directory-query">製品・機能を検索</label><input id="directory-query" type="search" data-filter-query placeholder="例：TestSprite、API、保守"></div><button type="button" data-filter-reset>検索をクリア</button><p data-filter-count role="status" aria-live="polite">40 / 40 件</p></div>
<p class="empty-state" data-filter-empty hidden>該当する製品がありません。検索語を変更してください。</p><ul class="directory-grid">{"".join(rows)}</ul></div>
<p class="muted">直接競合に加え、UX調査や内製用の実行基盤も含みます。画像・動画は公開素材と実操作の記録を区別し、製品ごとに確認範囲を記載しています。</p>'''


def comparison_notes(body):
    start = body.index("<h2>画面で先に見るべき比較</h2>")
    return '<h1>比較の見どころ</h1><p>製品ごとの画面・作業の流れを見るときの着眼点と、今回確認した範囲をまとめています。</p>' + body[start:]


def image_viewer():
    return '''<dialog id="image-viewer" aria-labelledby="image-title">
<div class="viewer-toolbar"><h2 id="image-title">画面を拡大</h2><a id="image-original" target="_blank" rel="noopener">元画像を開く</a><button type="button" id="image-close" autofocus>閉じる</button></div>
<p id="image-status" role="status" hidden></p><div class="viewer-scroll"><img id="image-full" alt=""></div></dialog>'''
