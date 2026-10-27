# 競合の画面・動画の証跡

確認日：2026年10月27日。[ギャラリー](gallery.html)・[全体比較](../../competitor-flows.md)・[製品別](../../competitor-products/README.md)。Autestは対象外。問い合わせ・予約・登録フォーム、一般的なHero、装飾映像は収録しない。

## 種別

| 表記 | 意味 |
| --- | --- |
| recorded-product-ui | 既存のログイン済み製品の読取操作を撮影。今回の新規テストの証明ではない |
| public-demo-ui | 公開サンプル／紹介UIの画面。任意対象への実行とは別 |
| official-ui-image / official-ui-example | 公式が掲載するUI画像、またはその表示を撮影。提供者の例 |
| official-diagram | 業務・概念図。製品内の実画面ではない |
| official-product-video | 公式ページから取得した操作を含む動画。自分で実行した結果ではない |
| official-ui-animation | 提供者が構成したUIの紹介アニメーション。実アカウントの実行ではない |
| official-concept-video | 変更管理の概念アニメーション。実UIの操作映像ではない |
| recorded-official-video / recorded-official-demo | 公開紹介動画・アニメーションの再生画面を連続撮影 |
| recorded-public-demo | 公開サンプルの操作、または生成された動画の再生を撮影 |

## 保存・撮影と確認

macOSのDia／EdgeをComputer Useで操作。製品名・表示内容を目視し、不要なホーム・フォーム・読み込み途中・重複画像を除外した。ブラウザchromeを切り取り、TestSpriteではアカウント行も切り取った。公式のUI画像は出典を保持してPNG化した。画像の内容を生成AIで補完していない。

取得した公式動画はH.264へ変換、最大幅1600px、速度を変更せず、音声を除いた。動画の切り出し画像はファイル名のtNNNが当保存動画の秒数。元動画の時刻とは限らない。Moは公開YouTubeの約0:33〜1:01の範囲を連続撮影した抜粋で、全編ではない。

Computer Useによる連続撮影は取得間隔を維持してMP4化した。15fps出力は元の取得頻度ではなく、取得間隔中の動きは保存されていない。QA.techは86枚／約26秒、Moは140枚の連続区間。滑らかなOS録画やダウンロードした原映像と区別する。

MP4はFFmpegで全体をデコードして終了コードを確認し、代表フレームを目視。公開の人物紹介、装飾映像、テスト対象モックだけの操作ガイドは操作動画の件数に含めない。アットストリームの26秒映像はモックの記録・再生デモと明記する。

TestNeoの認証文字列は公開テンプレートのサンプル。顧客の認証情報ではない。動画の一時アクセス値・セッションURLを出典一覧へ転記しない。

## 製品別の画像・動画一覧

保存画像161点（公式UI素材・業務図を含む）、動画22本、動画の切り出し画像73点。切り出しを独立した確認画面として二重加算しない。

| 製品 | 画像 | 動画 | 詳細 |
| --- | --- | --- | --- |
| TestSprite | 36 | 1 | [全画面・出典・動画の場面](../../competitor-products/testsprite.md) |
| QA.tech | 2 | 1 | [全画面・出典・動画の場面](../../competitor-products/qatech.md) |
| Momentic／Mo | 11 | 1 | [全画面・出典・動画の場面](../../competitor-products/momentic.md) |
| Touchstone | 0 | 1 | [全画面・出典・動画の場面](../../competitor-products/touchstone.md) |
| TestNeo | 12 | 1 | [全画面・出典・動画の場面](../../competitor-products/testneo.md) |
| Validate.QA | 6 | 0 | [全画面・出典・動画の場面](../../competitor-products/validate.md) |
| Canary | 1 | 0 | [全画面・出典・動画の場面](../../competitor-products/canary.md) |
| QA Wolf Platform | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/qawolf.md) |
| MagicPod本体 | 3 | 0 | [全画面・出典・動画の場面](../../competitor-products/magicpod.md) |
| Autify Aximo | 0 | 4 | [全画面・出典・動画の場面](../../competitor-products/autify.md) |
| Docket | 0 | 3 | [全画面・出典・動画の場面](../../competitor-products/docket.md) |
| Meticulous | 1 | 0 | [全画面・出典・動画の場面](../../competitor-products/meticulous.md) |
| Autosana | 0 | 1 | [全画面・出典・動画の場面](../../competitor-products/autosana.md) |
| QualGent | 3 | 0 | [全画面・出典・動画の場面](../../competitor-products/qualgent.md) |
| Spur | 1 | 0 | [全画面・出典・動画の場面](../../competitor-products/spur.md) |
| Revyl | 14 | 2 | [全画面・出典・動画の場面](../../competitor-products/revyl.md) |
| TesterArmy | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/testerarmy.md) |
| Swarm | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/swarm.md) |
| Tookii | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/tookii.md) |
| Uxia | 4 | 0 | [全画面・出典・動画の場面](../../competitor-products/uxia.md) |
| MagicPod AIテストセンター | 1 | 0 | [全画面・出典・動画の場面](../../competitor-products/magicpod-center.md) |
| SHIFT AIテストエージェント | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/shift.md) |
| AGEST QA for AI駆動開発 | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/agest.md) |
| アットストリーム | 3 | 1 | [全画面・出典・動画の場面](../../competitor-products/atstream.md) |
| TESTRA | 2 | 0 | [全画面・出典・動画の場面](../../competitor-products/testra.md) |
| mabl | 9 | 1 | [全画面・出典・動画の場面](../../competitor-products/mabl.md) |
| testRigor | 4 | 0 | [全画面・出典・動画の場面](../../competitor-products/testrigor.md) |
| Amikoo（MuukTest） | 1 | 0 | [全画面・出典・動画の場面](../../competitor-products/amikoo.md) |
| MuukTest Managed QA | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/muuktest-service.md) |
| Checksum | 2 | 0 | [全画面・出典・動画の場面](../../competitor-products/checksum.md) |
| TestDriver | 7 | 0 | [全画面・出典・動画の場面](../../competitor-products/testdriver.md) |
| Panaya Test Dynamix | 7 | 0 | [全画面・出典・動画の場面](../../competitor-products/panaya.md) |
| Testsigma／Atto | 6 | 0 | [全画面・出典・動画の場面](../../competitor-products/testsigma.md) |
| Katalon True Platform | 0 | 1 | [全画面・出典・動画の場面](../../competitor-products/katalon.md) |
| Tricentis Testim | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/testim.md) |
| UserTesting | 5 | 1 | [全画面・出典・動画の場面](../../competitor-products/usertesting.md) |
| Synthetic Users | 2 | 1 | [全画面・出典・動画の場面](../../competitor-products/synthetic-users.md) |
| Browser Use | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/browser-use.md) |
| KaneAI（TestMu AI） | 0 | 0 | [全画面・出典・動画の場面](../../competitor-products/kaneai.md) |
| BrowserStack AI（Test Management／LCA） | 18 | 2 | [全画面・出典・動画の場面](../../competitor-products/browserstack-ai.md) |

[manifest.json](manifest.json)に各ファイルの種別・掲載元・直接URL・SHA-256を記録する。提供者の画面は現行版と異なる場合がある。全製品の登録後の全画面を確認した資料ではない。
