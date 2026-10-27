# Tricentis Testim — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#testim)

## 調査範囲

Web・mobile・Salesforce向けの作成・保守・TestOps。Tricentis内のTosca・qTestとは別の製品として扱う。

比較上の位置：回帰自動化・既存QAの比較。追加理由：既存チームが使う記録・安定したUI認識・再利用・CIを代替候補から外さないため。

一次情報のoverviewは確認。ホームの直接取得は403、旧Tricentis製品URLは404。内部画面・操作動画は今回未収録で、非対応とは判断しない。

## 作業の流れ

対象 → recording／authoring → 検査・再利用部品 → local／cloud実行 → 結果 → locator・手順保守 → CI

## 機能の構成

公式overviewでWeb・Mobile・Salesforceを確認。詳細ナビ・実際の設定画面は今回未収録。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 入力 | 対象アプリ | Web・mobile・Salesforceの対象を扱う。 |
| 作成 | Low-code authoring | 操作フローを短時間で作成する製品説明。 |
| 拡張 | JavaScript・再利用 | 複雑な処理を挿入し、複数テストで共有できると説明。 |
| 安定化 | Smart locators | 機械学習による対象認識とUI変更への対応を訴求。 |
| 実行 | テストとDevOps | CI/CDへ接続して継続的に確認する。 |
| 管理 | TestOps | テストの管理・拡大を支える機能として説明。 |
| mobile | Device・app management | 端末・アプリ管理とlow-codeの作成体験を案内。 |
| 保守 | 変更対応 | 現行の修復・失敗レビュー・設定の具体的導線は未確認。 |

## 人の担当と比較上の着眼点

期待・検査の作成、拡張コード、テストと失敗・変更のレビュー。

調査者の解釈：AI探索だけに比較対象を寄せず、すでに稼働しているテスト資産と管理工程も比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

製品内の画面は未収録。公開説明に基づく機能表と、実際のUIを確認できた範囲を分けている。

## 一次情報

- [公式製品ページ](https://docs.tricentis.com/testim/content/overview/testim-overview/index.htm)
