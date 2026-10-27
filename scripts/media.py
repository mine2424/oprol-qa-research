"""Visible media previews backed by the collected source files."""

import html
import json
import os
from pathlib import Path
import re
import subprocess

SITE = Path(__file__).resolve().parents[1] / "site"
EVIDENCE = SITE / "competitor-evidence/2026-10-27"


def posters():
    result = {}
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    for video in manifest["videos"]:
        source = (EVIDENCE / "deep" / video["file"]).resolve()
        frames = video.get("frames", [])
        if frames:
            poster = EVIDENCE / "deep" / frames[0]["file"]
        else:
            poster = EVIDENCE / "posters" / (source.stem + ".jpg")
            poster.parent.mkdir(exist_ok=True)
            if not poster.exists():
                subprocess.run([
                    "ffmpeg", "-v", "error", "-ss", "1", "-i", str(source),
                    "-frames:v", "1", "-vf", "scale=960:-1", "-q:v", "3", str(poster),
                ], check=True)
        assert poster.exists(), poster
        result[source] = poster.resolve()
    return result


def video_preview(url, label, page, poster_paths):
    source = (page.parent / html.unescape(url)).resolve()
    poster = os.path.relpath(poster_paths[source], page.parent)
    title = html.escape(re.sub(r"<[^>]+>", "", html.unescape(label)), quote=True)
    return f'<span class="inline-video"><video controls playsinline preload="none" poster="{poster}" src="{url}" aria-label="{title}"></video><a href="{url}">{label}</a></span>'


def previews(body, page, poster_paths):
    image_urls = set()

    def anchor(match):
        url, label = match[1], match[2]
        if "<img" in label:
            return match[0]
        if url.endswith(".mp4"):
            return video_preview(url, label, page, poster_paths)
        image_urls.add(html.unescape(url))
        title = html.escape(re.sub(r"<[^>]+>", "", html.unescape(label)), quote=True)
        return f'<a class="inline-image" href="{url}"><img loading="lazy" src="{url}" alt="{title}"><span>{label}</span></a>'

    pattern = r'<a[^>]*href="([^"]+\.(?:png|jpg|mp4))"[^>]*>(.*?)</a>'
    body = re.sub(pattern, anchor, body, flags=re.S)
    # Selected screenshots at the bottom duplicate the now-visible full image list.
    def deduplicate(match):
        return "" if html.unescape(match[1]) in image_urls else match[0]
    return re.sub(r'<p>(?:<a[^>]*>)?<img[^>]*src="([^"]+)"[^>]*>(?:</a>)?</p>', deduplicate, body)


def directory_previews(text, page, poster_paths):
    images = re.findall(r'\]\(([^)]+\.png)\)', text)
    videos = re.findall(r'\[([^\]]+)\]\(([^)]+\.mp4)\)', text)
    items = []
    def relative(url):
        source = (SITE / "competitor-products" / url).resolve()
        return html.escape(os.path.relpath(source, page.parent), quote=True)
    if images:
        url = relative(images[0])
        items.append(f'<a class="inline-image" href="{url}"><img loading="lazy" src="{url}" alt="製品画面のプレビュー"><span>画面を拡大</span></a>')
    if videos:
        label, url = videos[0]
        items.append(video_preview(relative(url), html.escape(label), page, poster_paths))
    return '<div class="directory-previews">' + "".join(items) + '</div>' if items else ""
