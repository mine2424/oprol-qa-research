# Validate.QA — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#validate)

## 調査範囲

トップ内にSample dataと明記した操作型製品デモがある。実際の契約後アプリと区別。



サンプルを操作しただけで、任意URLへのSurveyや新規suite実行はしていない。Settingsは選択後に表示反映を確認できず、監査画面と重複した撮影は除外した。

## 作業の流れ

URL・認証 → Survey／Session → Features → Tests生成・検証 → Suite → Reports → Selector repair → Copilot／Knowledge／Audit → 再調査

## 機能の構成

Sessions / Tests / Test Data / API Intelligence / Site Intelligence / Selector Registry / Validate Copilot / Project Knowledge / Reports / AI Audit / Settings / Support。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 開始・探索 | Sessions | Survey、手動record、IDE接続、既存資産importの入口。探索結果を意図・機能にまとめる。 |
| ケース | Tests | 認証・フォーム等の24件サンプルを表示。HealedとPassedを分け、suite実行の入口を置く。 |
| データ | Test Data | 手順と実行データの管理を別のナビに置く。保存・秘密管理の実挙動は未確認。 |
| 分析 | API／Site Intelligence | 通信・画面の分析と所見。サンプルではCookie属性等のfindingがある。 |
| 修復 | Selector Registry | 修復前後のselectorと再実行の説明、修復済みテストへ移る入口。 |
| 相談・知識 | Validate Copilot・Project Knowledge | coverage、注意点、修復理由への質問と、プロジェクト知識の入口。 |
| 結果 | Reports | 実行履歴、成功率、所要時間、self-healed件数、修復前の実行を表示。 |
| 監査・設定 | AI Audit・Settings | 処理別のサンプルtokens・費用・時間、設定への入口。実費や保存の動作は未検証。 |

## 人の担当と比較上の着眼点

対象・認証を渡し、生成テストや修復差分・問題の妥当性を確認する。

調査者の解釈：探索結果、テスト、根拠、修復、AI処理の監査を行き来できる。入口だけの評価ではこの広さを見落とす。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [Tests：ケース一覧・Healed表示](../competitor-evidence/2026-10-27/deep/validate-12-tests.png) | public-demo-ui | [掲載元](https://validate.qa) |
| [Reports：履歴と修復前後](../competitor-evidence/2026-10-27/deep/validate-13-reports.png) | public-demo-ui | [掲載元](https://validate.qa) |
| [API Intelligence：所見](../competitor-evidence/2026-10-27/deep/validate-14-api.png) | public-demo-ui | [掲載元](https://validate.qa) |
| [Selector Registry：修復差分](../competitor-evidence/2026-10-27/deep/validate-15-selectors.png) | public-demo-ui | [掲載元](https://validate.qa) |
| [Validate Copilot：質問と根拠への入口](../competitor-evidence/2026-10-27/deep/validate-16-copilot.png) | public-demo-ui | [掲載元](https://validate.qa) |
| [AI Audit：処理別のtokens・費用（sample）](../competitor-evidence/2026-10-27/deep/validate-17-audit.png) | public-demo-ui | [掲載元](https://validate.qa) |

![Tests：ケース一覧・Healed表示 — public-demo-ui](../competitor-evidence/2026-10-27/deep/validate-12-tests.png)

![Reports：履歴と修復前後 — public-demo-ui](../competitor-evidence/2026-10-27/deep/validate-13-reports.png)

![API Intelligence：所見 — public-demo-ui](../competitor-evidence/2026-10-27/deep/validate-14-api.png)

## 一次情報

- [公式製品ページ](https://validate.qa/)
- [docs](https://validate.qa/docs)
- [how-it-works](https://validate.qa/how-it-works)
- [example-run](https://validate.qa/example-run)
