# Meticulous — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#meticulous)

## 調査範囲

記録した操作と決定的な再生でPRの前後差分を見るフロントエンド検証。



公開画面例と導入手順のみ。RecorderをOprolへ入れていない。Vimeoの再生は今回未収録。

## 作業の流れ

Recorder導入 → 開発・検証環境で操作記録 → CI・PR接続 → セッション選定・再生 → 基準commitとの差分 → 人／Agentが確認

## 機能の構成

公式ページはInstall / Execute / Review。製品画面例はUI Differencesの左右比較とApprove。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 導入 | Recorder snippet | 内部の開発・検証環境への導入を推奨。ブラウザ操作を記録する。 |
| 収集 | Recorded sessions | 人や開発Agentの通常操作をテスト候補にする。 |
| 接続 | CI・PR permissions | PR／MRへ結果を投稿する接続を用意する。 |
| 選定 | Coverage・curation | 記録セッションから変更に関係するフローを選び、継続的に集合を更新する。 |
| 実行 | Deterministic replay | 記録イベントを再生し、各時点の画面を基準commitと比較する。 |
| 境界 | Backend replay | 標準では保存済みの通信応答を再利用する。実backendの毎回の動作確認とは範囲が異なる。 |
| 結果 | Visual diffs | 前後の画面差分をPRと製品画面から確認する。 |
| 運用 | Review・agent loop | 差分の意図・妥当性を判断し、修正と再確認へ進む。 |

## 人の担当と比較上の着眼点

Recorder・CIの導入と、意図した差分かどうかのレビュー。

調査者の解釈：テストを書く負担を操作記録で置き換える。探索能力の比較とは分け、backend応答再利用の範囲を明示する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [Dashboard](../competitor-evidence/2026-10-27/deep/meticulous-vendor-06.png) | official-ui-image | [掲載元](https://www.meticulous.ai/) |

![Dashboard — official-ui-image](../competitor-evidence/2026-10-27/deep/meticulous-vendor-06.png)

## 一次情報

- [公式製品ページ](https://www.meticulous.ai/)
- [how-it-works](https://www.meticulous.ai/how-it-works)
- [docs](https://app.meticulous.ai/docs)
