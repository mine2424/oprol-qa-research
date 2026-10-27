# QualGent — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#qualgent)

## 調査範囲

TrustLoop、DevLoop、Enterpriseの3系統を同じ品質循環にまとめる。旧来のモバイルテスト作成だけでは範囲を捉えきれない。



公式の画面素材と説明。実機・MCP・振分け・修正確認は未操作。表示されたqueueは自分の実行結果ではない。

## 作業の流れ

実利用を記録 → 不具合・再現・回帰候補 → DevLoopで開発中に検証 → Enterpriseで人／AIへ分配 → 統合結果 → 次回の知識

## 機能の構成

TrustLoop（mobile bug capture）/ DevLoop（device control・MCP）/ Enterprise（Test Run Queue・統合判断）。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 収集 | TrustLoop | 実利用の録画、画面遷移、端末・OS・地域・メモを捕捉する。 |
| 変換 | Bug report | 記録を再現手順・画像・テストケースにまとめる。 |
| 共有 | Notion・Jira・Linear・Slack | 報告を開発側の既存ツールへ渡す。 |
| 開発検証 | DevLoop | Agentが端末・simulatorでtap・swipe・inspectして変更を確かめる。 |
| 委任 | MCP | コーディングAgentから端末検証を使う入口を案内する。 |
| 振分け | Enterprise fan-out | リスクや曖昧さに応じ、人・AI・端末・既存工程へテストを分配する。 |
| 結果 | Test Run Queue・release view | passed／failed／review必要等を集約する画面例。 |
| 知識 | Regression memory | 捕捉したbugと結果を次回の検証へ戻す閉ループを説明する。 |

## 人の担当と比較上の着眼点

実利用の問題を捕捉し、曖昧・主観的・高リスクな検証を人が判断する。

調査者の解釈：人の判断が必要な検証をどこに残すか、不具合記録が次の回帰へどう変わるかを比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [TrustLoop recording screen](../competitor-evidence/2026-10-27/deep/qualgent-vendor-10.png) | official-ui-image | [掲載元](https://www.qualgent.ai/) |
| [DevLoop agent testing interface](../competitor-evidence/2026-10-27/deep/qualgent-vendor-11.png) | official-ui-image | [掲載元](https://www.qualgent.ai/) |
| [QualGent Enterprise dashboard](../competitor-evidence/2026-10-27/deep/qualgent-vendor-12.png) | official-ui-image | [掲載元](https://www.qualgent.ai/) |

![TrustLoop recording screen — official-ui-image](../competitor-evidence/2026-10-27/deep/qualgent-vendor-10.png)

![DevLoop agent testing interface — official-ui-image](../competitor-evidence/2026-10-27/deep/qualgent-vendor-11.png)

![QualGent Enterprise dashboard — official-ui-image](../competitor-evidence/2026-10-27/deep/qualgent-vendor-12.png)

## 一次情報

- [公式製品ページ](https://www.qualgent.ai/)
