# Browser Use — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#browser-use)

## 調査範囲

Cloud browser・Agent APIとOSS libraryを区別する参考枠。QAの要求・承認・不具合管理を一式提供する直接競合と同列にしない。

比較上の位置：実行基盤・内製代替の参考。追加理由：顧客が開発Agentとbrowser基盤を組み合わせて内製する代替手段を把握するため。

Docsのみ。CloudやOSS Agentを起動していない。OSS libraryとCloud APIの呼出し・料金・能力を合成しない。

## 作業の流れ

browser／profile・secrets → goal／task → events・live preview → human takeover → 結果／recording・files → script再実行

## 機能の構成

Cloud browser、Agent task／session、profiles、workspaces、observability、live preview。アカウント内のdashboardは未操作。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 環境 | Cloud browser | hosted Chromiumに接続して操作する実行基盤。 |
| 指示 | Agent task | 目的を与え、Agentにbrowser操作を委ねるAPI。 |
| 認証・準備 | Profiles・secrets | browser状態とrunに渡す認証情報を管理する説明。 |
| 進捗 | Events・observability | 実行イベントを追い、独自UIや監視へ接続する。 |
| 介入 | Human in the loop | live browserを人が引き取り、同じsessionで継続する。 |
| 証拠 | Live preview・recording | 実行を閲覧・記録するための入口。 |
| 再利用 | Scripts・workspaces | 処理やfileを次の実行へ引き継ぐ機能。 |
| QAとの境界 | 顧客が組み立てる部分 | 要求の正解、承認、coverage、不具合判定等は独立して用意・検証が必要。 |

## 人の担当と比較上の着眼点

目的、操作権限、予算、期待の根拠、結果の妥当性を自前の検証工程で管理する。

調査者の解釈：実行能力を調達するコストと、QA業務全体を製品化する価値を分けて比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

製品内の画面は未収録。公開説明に基づく機能表と、実際のUIを確認できた範囲を分けている。

## 一次情報

- [公式製品ページ](https://browser-use.com/)
- [browser-use-doc-quickstart.md](https://docs.browser-use.com/cloud/agent/quickstart)
- [browser-use-doc-human-in-the-loop.md](https://docs.browser-use.com/cloud/agent/human-in-the-loop)
- [browser-use-doc-live-preview.md](https://docs.browser-use.com/cloud/browser/live-preview)
