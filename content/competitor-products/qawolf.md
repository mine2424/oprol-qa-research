# QA Wolf Platform — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#qawolf)

## 調査範囲

Platformのテスト計画・自動化・実行基盤と、人が担当するServiceを分ける。



公開のworkflowアニメーションのみ操作確認。ログイン後の編集・失敗調査・スケジュール・権限設定は未操作。

## 作業の流れ

対象アプリ → フロー把握・計画 → Agentで作成 → Playwright／Appium → 手動／schedule／deploy → 失敗調査 → バグ報告・保守

## 機能の構成

PlatformのMapping / AI Automation / AI Run Infra。DocsにTest Planning / Test Automation / Triggers / Smart Smoke Suites / MCP / Integrations。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 範囲 | Test Planning・Mapping | ユーザーフローをテスト計画へ整理し、確認範囲を管理する。 |
| 作成 | AI Automation | AgentがWebはPlaywright、モバイル等はAppiumでテストを作る。 |
| 実行 | Run infrastructure | スイートを並列実行する基盤。手動・スケジュール・デプロイ契機を扱う。 |
| 選定 | Smart Smoke Suites | 変更に応じた検証集合を扱う。選定精度は未評価。 |
| 失敗調査 | Investigation | 失敗を調べ、テスト側の問題と製品側の問題を扱うと説明。 |
| 報告・保守 | Bug report・maintenance | 根拠付き報告とテスト維持を同じサイクルで提供。 |
| 連携 | MCP・GitHub／Slack等 | 開発Agent、PR、チャットから作成・実行へ接続。独自skillsも文書化。 |

## 人の担当と比較上の着眼点

対象・範囲・期待の決定。Service契約ではどの作業を人が引き取るか別途確認する。

調査者の解釈：作成単価だけでなく、原因調査・保守・実行環境と人のサービスの費用を含めて比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

製品内の画面は未収録。公開説明に基づく機能表と、実際のUIを確認できた範囲を分けている。

## 一次情報

- [公式製品ページ](https://www.qawolf.com/)
- [Test Automation](https://docs.qawolf.com/test-automation)
- [Triggers](https://docs.qawolf.com/triggers/overview)
- [Smart Smoke Suites](https://docs.qawolf.com/smart-smoke-suites)
- [Test QR code authentication](https://docs.qawolf.com/qrcode)
- [Pass data between flows](https://docs.qawolf.com/Pass-data-between-flows)
- [Integrations](https://docs.qawolf.com/integrations)
