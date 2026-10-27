"""Presentation helpers; research claims remain in the source documents."""

import html
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


def directory(poster_paths):
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
        page = CONTENT.parent / "site/competitor-products/README.html"
        media = directory_previews(text, page, poster_paths)
        rows.append(f'''<li class="directory-card" data-filter-item>
<h2><a href="{slug}.html">{html.escape(name)}</a></h2>
<p class="directory-scope">{html.escape(scope)}</p>
{media}
<p class="media-count">{html.escape(cells[-2])}</p>
<div class="directory-links"><a href="{slug}.html" aria-label="{html.escape(name)}の詳細を読む">詳細を読む</a><a href="../competitor-evidence/2026-10-27/gallery.html#{slug}" aria-label="{html.escape(name)}の画像・動画を見る">画像・動画</a></div></li>''')
    return f'''<h1>製品別の機能・導線調査</h1>
<p class="page-intro">40製品／サービスの調査範囲と資料を探せます。製品名や機能で絞り込んでください。</p>
<p class="muted">画像数は公式素材・業務図を含みます。数は性能や確認の網羅率を示すものではありません。</p>
<div data-filter-root><div class="filter-bar"><div><label for="directory-query">製品・機能を検索</label><input id="directory-query" type="search" data-filter-query placeholder="例：TestSprite、API、保守"></div><button type="button" data-filter-reset>検索をクリア</button><p data-filter-count role="status" aria-live="polite">40 / 40 件</p></div>
<p class="empty-state" data-filter-empty hidden>該当する製品がありません。検索語を変更してください。</p><ul class="directory-grid">{"".join(rows)}</ul></div>'''


def comparison(body):
    pattern = r'<div class="table-scroll"[^>]*><table>(.*?)</table></div>'

    def table(match):
        rows = re.findall(r'<tr>(.*?)</tr>', match[1], re.S)
        rows_html = "".join(f'<tr data-filter-item>{row}</tr>' for row in rows[1:])
        return f'''<div data-filter-root class="comparison-root">
<div class="filter-bar"><div><label for="comparison-query">比較する製品・機能を検索</label><input id="comparison-query" type="search" data-filter-query placeholder="例：TestNeo、API、回帰"></div><button type="button" data-filter-reset>検索をクリア</button><p data-filter-count role="status" aria-live="polite">40 / 40 件</p></div>
<p class="table-hint">表は縦・横にスクロールできます。製品名と見出しは固定しています。</p>
<div class="evidence-legend"><span>R 実画面</span><span>S 公開サンプル</span><span>V 公式画面・動画</span><span>D 文書</span><span>U 未確認</span></div>
<p class="empty-state" data-filter-empty hidden>該当する製品がありません。検索語を変更してください。</p>
<div class="table-scroll comparison-table" role="region" aria-label="40製品の機能・導線比較。縦と横にスクロールできます" tabindex="0"><table><thead><tr>{rows[0]}</tr></thead><tbody>{rows_html}</tbody></table></div></div>'''

    body = re.sub(pattern, table, body, count=1, flags=re.S)
    names = {"R": "実画面", "S": "公開サンプル", "V": "公式画面・動画", "D": "文書", "U": "未確認"}
    for code, label in names.items():
        body = body.replace(f'<td>{code}</td>', f'<td><abbr class="evidence evidence-{code.lower()}" title="{label}" aria-label="{label}">{code}</abbr></td>')
    return body


def overview(body):
    def documents(match):
        rows = re.findall(r"<tr>(.*?)</tr>", match[1], re.S)[1:]
        items = []
        for row in rows:
            cells = re.findall(r"<td>(.*?)</td>", row, re.S)
            items.append(f'<li><div class="document-name">{cells[0]}</div><p>{cells[1]}</p><span>{cells[2]}</span></li>')
        return '<ul class="document-list">' + "".join(items) + '</ul>'

    pattern = r'<div class="table-scroll"[^>]*><table>(.*?)</table></div>'
    return re.sub(pattern, documents, body, count=1, flags=re.S)


def image_viewer():
    return '''<dialog id="image-viewer" aria-labelledby="image-title">
<div class="viewer-toolbar"><h2 id="image-title">画面を拡大</h2><a id="image-original" target="_blank" rel="noopener">元画像を開く</a><button type="button" id="image-close" autofocus>閉じる</button></div>
<p id="image-status" role="status" hidden></p><div class="viewer-scroll"><img id="image-full" alt=""></div></dialog>'''
