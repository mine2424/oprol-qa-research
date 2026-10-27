# Spur — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#spur)

## 調査範囲

探索・機能・UI/UX・ローカライズ・AI機能の専門AgentとWeb／モバイル。公開Bug Bookで報告形式を確認できる。



公開Bug Bookを撮影。実アカウントの作成・実行・設定、モバイル、修復は未操作。公開の重大度は当調査の評価ではない。

## 作業の流れ

対象・意図 → 専門Agent → 実操作 → finding・根拠 → bug report → 開発工程／MCP → 再確認

## 機能の構成

AI Agents / Mobile QA / MCP / Bug Book / Case Studies。アカウント内の一覧・設定ナビは未確認。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 設定 | Intent・Functional agent | ユーザーが達成できるべき行動を自然言語で定義する。 |
| 探索 | Exploratory agent | 決まった経路以外の不具合探索を案内する。 |
| 専門検証 | Localization・UI/UX・AI feature | 機能成否だけでなく文言・見た目・AI応答等の目的を分ける。 |
| 対象 | Web・Native mobile | ネイティブアプリのビルドと操作を案内。具体的端末条件は契約時に確認。 |
| 報告 | Bug Book | 公開例は問題・利用Agent・影響・再現根拠をまとめる。 |
| 接続 | MCP | 開発Agentからケース作成・実行・結果確認に接続する説明。 |
| 継続 | CI・開発工程 | 定期・変更に合わせた確認を案内。実際の保守・実行設定は未操作。 |

## 人の担当と比較上の着眼点

検証の意図、対象、ローカライズ等の正しい期待、報告の妥当性を確認する。

調査者の解釈：Agentの種類の多さより、同じfindingに何の根拠と再現手順が付くかを見る。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [公開Bug Book：問題・影響・根拠](../competitor-evidence/2026-10-27/deep/spur-10-bug-report.png) | official-ui-example | [掲載元](https://www.spurtest.com/bug-book/checkout-button-leads-to-error-page) |

![公開Bug Book：問題・影響・根拠 — official-ui-example](../competitor-evidence/2026-10-27/deep/spur-10-bug-report.png)

## 一次情報

- [公式製品ページ](https://www.spurtest.com/)
- [exploratory-testing](https://www.spurtest.com/agents/exploratory-testing)
- [functional-testing](https://www.spurtest.com/agents/functional-testing)
- [mobile-qa](https://www.spurtest.com/mobile-qa)
- [spur-mcp](https://www.spurtest.com/spur-mcp)
- [checkout-button-leads-to-error-page](https://www.spurtest.com/bug-book/checkout-button-leads-to-error-page)
