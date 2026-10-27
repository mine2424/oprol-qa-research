# TestSprite — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#testsprite)

## 調査範囲

Web PortalのUI/APIテスト、CLI/MCP、継続実行。既存サンプルを読取操作し、探索・生成は公式文書の画面で補完。



既存サンプルの過去実行を閲覧した。今回の新規テスト・Auto-Heal・PR接続・通知送信は未実施。公式文書のUIと現在の既存プロジェクトのUIに差がある。

## 作業の流れ

Workspace → Project作成 → URL・認証・資料 → 探索 → 計画編集 → 生成・実行 → 結果／Agent Action → 修正・再実行 → List／Schedule／PR

## 機能の構成

Workspace: Overview / Chats / All Projects / Test Lists / Test Schedules / General / Members / Billing / Integrations。Project: Sources / Test Cases / Test Runs / Insights / Activity / Environment / Run Behavior / Test Files / Notifications。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 開始 | New Project・Sources | Frontend／Backendの種類、URL、任意のPRD、認証方法を設定する。資料がない経路もある。 |
| 理解 | Feature Exploration・Coverage Map | 探索中の対象ブラウザとAgentの操作、訪問画面を表示。機能のまとまりを計画へ渡す。 |
| 設計 | Test Plan・Test Cases | 生成案の目的・優先度を編集して、作成対象を選ぶ。計画と生成済みのケースを分ける。 |
| 実行 | Test Runs | ケースを生成・実行し状態で絞る。既存環境では4ケースと4実行、全件／失敗のみ再実行の入口を確認。 |
| 判断 | List View・Agent Action View | 結果を表とページマップで切り替える。失敗ケース、レポート、編集への入口を置く。 |
| 保守 | Auto-Heal・Edit & Re-run | 公式文書は自動修復と手動編集後の再実行を説明。今回は新規修復を発行していない。 |
| 運用 | Environment・Run Behavior・Test Files | 環境を資産化し、実行時の振る舞い・アップロード用ファイルを別管理する。 |
| 連携・管理 | Test Lists・Schedules・GitHub・共有 | プロジェクトを越える実行集合、定期実行、PRトリガー、メンバー・共有権限を扱う。 |
| APIの発見 | API Discovery | API資料・稼働endpointを基に、endpoint候補を確認して計画へ進む。 |
| APIの作成 | Endpoint／Integration tests | 個別endpointと、前のresponseを次のrequestへ渡す複数段のフローを分けて生成する。 |
| APIのデータ | Dynamic Variables・Dependencies | レスポンスから得たID等を引き継ぎ、依存するテストの順序とデータを扱う。 |
| APIの運用 | Auto Auth・Auto Cleanup | 認証と作成データの後始末を扱うと公式Docsに記載。自社backendでは実行していない。 |
| UIの証拠 | Step-by-Step Replay | actionごとのHTML snapshotと録画を切り替え、失敗stepの対象画面と操作を調べる。 |

## 人の担当と比較上の着眼点

URL・認証・業務上の期待、生成計画のレビュー、失敗原因と修復の妥当性を判断する。

調査者の解釈：チャット、計画、実行結果、環境設定を別の資産としてつなぐ。Oprolでも初回作成だけでなく、失敗から編集・再実行へ戻る導線を比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

- [公開Live run紹介の連続撮影](../competitor-evidence/2026-10-27/deep/../testsprite-live-run.mp4)（17.5秒、recorded-public-demo）。[公式の掲載元](https://www.testsprite.com/)。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [Overview：Workspace全体](../competitor-evidence/2026-10-27/deep/testsprite-vendor-29.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/getting-started/overview) |
| [Sources：PRDを使う入力](../competitor-evidence/2026-10-27/deep/testsprite-vendor-30.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/getting-started/overview) |
| [Project設定：URL・認証・Sources](../competitor-evidence/2026-10-27/deep/testsprite-vendor-32.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/quickstart) |
| [Feature Exploration：探索中](../competitor-evidence/2026-10-27/deep/testsprite-vendor-33.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/quickstart) |
| [Test Coverage：機能から計画へ](../competitor-evidence/2026-10-27/deep/testsprite-vendor-34.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/quickstart) |
| [探索：ライブ対象とAgentの操作](../competitor-evidence/2026-10-27/deep/testsprite-vendor-35.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/feature-exploration) |
| [探索：訪問画面とstep](../competitor-evidence/2026-10-27/deep/testsprite-vendor-36.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/feature-exploration) |
| [Sources：探索後の画面一覧](../competitor-evidence/2026-10-27/deep/testsprite-vendor-37.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/feature-exploration) |
| [Environment一覧：Dev／Staging／Prod](../competitor-evidence/2026-10-27/deep/testsprite-vendor-38.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/setup/environments) |
| [Environment追加：URLと設定](../competitor-evidence/2026-10-27/deep/testsprite-vendor-40.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/setup/environments) |
| [Coverage Map：機能とケース](../competitor-evidence/2026-10-27/deep/testsprite-vendor-41.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/working-with-test/coverage-map) |
| [Coverage Map：ケース編集](../competitor-evidence/2026-10-27/deep/testsprite-vendor-42.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/working-with-test/coverage-map) |
| [Test Lists：実行集合の一覧](../competitor-evidence/2026-10-27/deep/testsprite-vendor-44.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/maintenance/test-lists) |
| [Test List：ケース追加](../competitor-evidence/2026-10-27/deep/testsprite-vendor-46.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/maintenance/test-lists) |
| [GitHub：PRへの実行報告](../competitor-evidence/2026-10-27/deep/testsprite-vendor-47.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/integrations/github-integration) |
| [GitHub：チェックと結果](../competitor-evidence/2026-10-27/deep/testsprite-vendor-48.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/integrations/github-integration) |
| [Share：アクセスできる人](../competitor-evidence/2026-10-27/deep/testsprite-vendor-50.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/admin/sharing) |
| [Share：招待先と役割](../competitor-evidence/2026-10-27/deep/testsprite-vendor-52.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/admin/sharing) |
| [APIの準備・endpoint探索・実行 1](../competitor-evidence/2026-10-27/deep/testsprite-extra-quickstart-1.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/api/quickstart) |
| [APIの準備・endpoint探索・実行 2](../competitor-evidence/2026-10-27/deep/testsprite-extra-quickstart-2.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/api/quickstart) |
| [APIの準備・endpoint探索・実行 3](../competitor-evidence/2026-10-27/deep/testsprite-extra-quickstart-3.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/api/quickstart) |
| [APIの準備・endpoint探索・実行 4](../competitor-evidence/2026-10-27/deep/testsprite-extra-quickstart-4.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/api/quickstart) |
| [ステップのHTML・録画のリプレイ 1](../competitor-evidence/2026-10-27/deep/testsprite-extra-ui-step-by-step-1.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/ui-step-by-step) |
| [ステップのHTML・録画のリプレイ 2](../competitor-evidence/2026-10-27/deep/testsprite-extra-ui-step-by-step-2.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/ui-step-by-step) |
| [ステップのHTML・録画のリプレイ 3](../competitor-evidence/2026-10-27/deep/testsprite-extra-ui-step-by-step-3.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/ui-step-by-step) |
| [ステップのHTML・録画のリプレイ 4](../competitor-evidence/2026-10-27/deep/testsprite-extra-ui-step-by-step-4.png) | official-ui-image | [掲載元](https://docs.testsprite.com/web-portal/core/ui/ui-step-by-step) |
| [Workspace overview](../competitor-evidence/2026-10-27/deep/testsprite-10-overview.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [All Projects](../competitor-evidence/2026-10-27/deep/testsprite-11-projects.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [Test Cases：状態・優先度・編集／実行](../competitor-evidence/2026-10-27/deep/testsprite-12-test-cases.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [Test Runs：実行履歴・再実行入口](../competitor-evidence/2026-10-27/deep/testsprite-13-runs.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [Agent Action View：ページマップ](../competitor-evidence/2026-10-27/deep/testsprite-14-failure.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [List View：失敗ケース](../competitor-evidence/2026-10-27/deep/testsprite-15-run-list.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [Environments：実行先](../competitor-evidence/2026-10-27/deep/testsprite-16-environments.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [Run Behavior：実行設定](../competitor-evidence/2026-10-27/deep/testsprite-17-run-behavior.png) | recorded-product-ui | [掲載元](https://www.testsprite.com/) |
| [公開Copilot：レポートと会話](../competitor-evidence/2026-10-27/deep/../testsprite-02-copilot.png) | public-demo-ui | [掲載元](https://www.testsprite.com/) |
| [公開Live run：進捗とページマップ](../competitor-evidence/2026-10-27/deep/../testsprite-03-live-run.png) | public-demo-ui | [掲載元](https://www.testsprite.com/) |

![Project設定：URL・認証・Sources — official-ui-image](../competitor-evidence/2026-10-27/deep/testsprite-vendor-32.png)

![Test Cases：状態・優先度・編集／実行 — recorded-product-ui](../competitor-evidence/2026-10-27/deep/testsprite-12-test-cases.png)

![List View：失敗ケース — recorded-product-ui](../competitor-evidence/2026-10-27/deep/testsprite-15-run-list.png)

## 一次情報

- [公式製品ページ](https://www.testsprite.com/)
- [Overview](https://docs.testsprite.com/web-portal/getting-started/overview)
- [Quickstart](https://docs.testsprite.com/web-portal/core/ui/quickstart)
- [Feature Exploration](https://docs.testsprite.com/web-portal/core/ui/feature-exploration)
- [Auto-Heal](https://docs.testsprite.com/web-portal/core/ui/auto-heal)
- [Environments](https://docs.testsprite.com/web-portal/setup/environments)
- [Coverage Map](https://docs.testsprite.com/web-portal/core/working-with-test/coverage-map)
- [Test Lists](https://docs.testsprite.com/web-portal/maintenance/test-lists)
- [Test Lists & Schedules](https://docs.testsprite.com/cli/integrations/test-lists-and-schedules)
- [GitHub Integration](https://docs.testsprite.com/web-portal/integrations/github-integration)
- [Sharing a Project](https://docs.testsprite.com/web-portal/admin/sharing)
- [API Quickstart](https://docs.testsprite.com/web-portal/core/api/quickstart)
- [Step-by-Step Replay](https://docs.testsprite.com/web-portal/core/ui/ui-step-by-step)
