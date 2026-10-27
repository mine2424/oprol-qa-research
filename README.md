# Oprol QA Research

競合・代替手段の調査資料をブラウザで閲覧するための静的サイトです。

公開URL: https://mine2424.github.io/oprol-qa-research/

## 更新

`content/` のMarkdownが本文、`site/competitor-evidence/` が画像・動画と出典です。製品本体のコード・社内の資金計画は含めません。競合の公開情報は資料内の確認日を基準とし、現在の機能・価格を保証するものではありません。

`gh` にログインした環境で `python3 scripts/build.py` を実行します。GitHubのMarkdown APIでHTMLを生成し、`site/` に出力します。依存パッケージ・CIワークフローはありません。

`source` は管理用、`gh-pages` は `site/` の内容だけを置く公開用ブランチです。GitHub Pagesは `gh-pages` のルートから公開します。

各社の画面・映像など第三者素材の権利は各権利者に帰属します。出典は各製品ページと証跡一覧に記載しています。このリポジトリは第三者素材への利用許諾を付与しません。
