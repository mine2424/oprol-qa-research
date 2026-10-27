# Amikoo（MuukTest） — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#amikoo)

## 調査範囲

Amikoo製品とMuukTestの人を含む代行サービスを別行に分ける。現行トップはworker・PR・継続検証を強調。

比較上の位置：探索・PR検証の直接比較。追加理由：coverage gapの発見から自社repoのPlaywright生成・修復までが初期顧客の仕事と重なるため。

公開説明とチャットの画面例まで。旧チュートリアルの一部URLは404。旧名称のAgent群を現在のworker実装と合成しない。

## 作業の流れ

App・repo・資料 → scopeとcoverage → workerのtrigger・仕事・通知先 → Playwright生成 → PRで実行 → failureの診断 → 修復・再実行／bug登録

## 機能の構成

現在の公開説明にTest generator／Auto-fixer／Defect loggerのworkers、coverage map、chat。旧Designer／Explorer等の説明とは区別。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 接続 | App・Repository・資料 | 対象URLと権限、GitHub／Azure等のrepo、仕様・チケット等を文脈にする。 |
| 範囲 | Strategy・coverage map | チャットで対象範囲を決め、重要なcoverage gapを扱う。 |
| 自動化 | Workers | 発火条件、依頼する仕事、通知先を設定する説明。 |
| 生成 | Test generator | 変更と既存機能向けに標準Playwright TypeScriptを作り、repoへ残す。 |
| 実行 | Pull request・継続 | PRごとにテストを動かし、開発工程へ結果を返す。 |
| 診断 | Product bug／broken test | 製品の問題とテスト側の問題を分ける役割を案内。 |
| 修復 | Auto-fixer | 壊れたテストを修復して再実行するworker。 |
| 報告 | Defect logger | 製品不具合と確認した内容を記録する。出力先・承認条件の実UIは未確認。 |

## 人の担当と比較上の着眼点

対象・操作権限・期待と検証scope、生成コード・PR・不具合の妥当性を判断する。

調査者の解釈：専任QA不足、標準コードの所有、PRごとの継続検証の3軸で優先して比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [Chat：coverage不足からscriptを依頼する入口](../competitor-evidence/2026-10-27/deep/amikoo-extra-09.png) | official-ui-image | [掲載元](https://amikoo.ai/) |

![Chat：coverage不足からscriptを依頼する入口 — official-ui-image](../competitor-evidence/2026-10-27/deep/amikoo-extra-09.png)

## 一次情報

- [公式製品ページ](https://amikoo.ai/)
- [amikoo-3](https://muuktest.com/approach/ai-automation-services)
