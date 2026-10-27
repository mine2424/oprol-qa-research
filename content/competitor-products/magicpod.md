# MagicPod本体 — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#magicpod)

## 調査範囲

Web／モバイルのノーコード資産管理と、Autopilotによる作成・編集支援。AIテストセンターは別ページ。



機能ページを撮影。アカウント内の作成・端末接続・再実行・修復は未操作。Autopilot利用条件は契約時に確認。

## 作業の流れ

組織・Project → 対象／端末準備 → UI取得・操作記録／Autopilot → 手順編集 → 実行 → 画像・結果 → 共有部品／修復 → CI・通知

## 機能の構成

テスト作成 / テスト実行 / メンテナンス効率 / 連携。詳細は機能一覧とAutopilotの公式ページで補完。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 作成 | UI認識・記録 | 対象画面から操作・確認コマンドをノーコードで組み立てる。 |
| AI支援 | Autopilot | 自然言語からフローを作成し、既存テストの変更にも使う。 |
| 構成 | 変数・条件分岐・共通部品 | 入力条件・再利用手順を管理し、複数ケースへ展開する。 |
| 実行 | クラウド・端末 | Web・モバイルの実行環境、並列実行等を案内。 |
| 結果 | 実行結果・画像 | ケースとステップの成否を確認し、問題箇所を調べる。 |
| 保守 | UI変更への対応 | UI認識・共有部品・AI支援を使って継続テストを維持する。 |
| 運用 | CI・API・通知 | 外部からの実行、Slack等への通知、組織・プロジェクト運用を扱う。 |

## 人の担当と比較上の着眼点

期待や検査の設計、手順・共通部品の管理、結果レビュー。

調査者の解釈：自然言語の作成だけでなく、変数・条件分岐・共通部品・実行環境まで運用の比較対象になる。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [Hotel booking flow in one prompt](../competitor-evidence/2026-10-27/deep/magicpod-vendor-hotel-booking.png) | official-ui-image | [掲載元](https://magicpod.com/en/features/magicpod-autopilot/) |
| [Create a user registration test for a mobile app](../competitor-evidence/2026-10-27/deep/magicpod-vendor-user-registration.png) | official-ui-image | [掲載元](https://magicpod.com/en/features/magicpod-autopilot/) |
| [Add conditional logic to an existing test](../competitor-evidence/2026-10-27/deep/magicpod-vendor-conditional-branch.png) | official-ui-image | [掲載元](https://magicpod.com/en/features/magicpod-autopilot/) |

![Hotel booking flow in one prompt — official-ui-image](../competitor-evidence/2026-10-27/deep/magicpod-vendor-hotel-booking.png)

![Create a user registration test for a mobile app — official-ui-image](../competitor-evidence/2026-10-27/deep/magicpod-vendor-user-registration.png)

![Add conditional logic to an existing test — official-ui-image](../competitor-evidence/2026-10-27/deep/magicpod-vendor-conditional-branch.png)

## 一次情報

- [公式製品ページ](https://magicpod.com/en/)
- [機能詳細](https://magicpod.com/en/features/)
- [機能詳細](https://magicpod.com/en/features/magicpod-autopilot/)
