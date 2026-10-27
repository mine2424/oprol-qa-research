# testRigor — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#testrigor)

## 調査範囲

Web・モバイル等のsuiteと平易な英語のケース。公式サポートのAPI＋UIの例で作成から実行詳細まで確認。

比較上の位置：自然言語テスト・回帰の直接比較。追加理由：自然言語の手順、認証、APIとUIの接続、実行証跡までを同じsuiteで扱うため。

公式UI素材まで。自社対象の生成・実行は未実施。取得したサポート記事内の画像には過去UIが含まれ、現行画面との一致は未確認。

## 作業の流れ

Suite（URL・認証・OS/browser）→ App Descriptionまたはcustom case → 自然言語・API手順 → 実行 → View Execution → 画像・log・録画 → 修正・再実行

## 機能の構成

Test Suites、Test Cases、Reports／Errors／Test View／Visual Diff等の公式画面例。サンプル対象サイトの画像は製品画面として除外。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 準備 | Create Test Suite | 種類、対象URL、任意の認証情報、OS・browserを設定する。 |
| 作成 | AI生成・Custom Test Case | アプリ説明から生成する経路と、人が手順を書く経路を用意。 |
| 手順 | Plain English | クリック・入力・検査を文章で記述し、業務フローを構成する。 |
| API | API call・stored value | APIの戻り値を変数へ保存し、その値をUI入力に引き継ぐ。 |
| 実行 | Suite・case実行 | ケースを実行し、状態・時間・失敗箇所を確認する。 |
| 証拠 | View Execution | step画像、エラー、log、録画を参照する公式説明。 |
| 報告 | PDF／Word出力 | 実行stepと画像を文書へ出す入口を説明する。 |
| 保守 | 手順編集・再実行 | 文章のケースを修正して確認を繰り返す。自動修復の個別挙動は未確認。 |

## 人の担当と比較上の着眼点

手順の期待、データ・認証、生成ケースのレビュー、失敗と保守の判断。

調査者の解釈：自然言語の入口だけでなく、APIのデータ受渡しと結果の持ち出しを比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [Suite設定：種類・URL・認証・OS／browser](../competitor-evidence/2026-10-27/deep/testrigor-extra-01.png) | official-ui-image | [掲載元](https://support.testrigor.com/support/solutions/articles/154000231623-how-to-do-api-testing-using-testrigor-) |
| [Test Cases：custom caseの追加](../competitor-evidence/2026-10-27/deep/testrigor-extra-02.png) | official-ui-image | [掲載元](https://support.testrigor.com/support/solutions/articles/154000231623-how-to-do-api-testing-using-testrigor-) |
| [ケース編集：APIの戻り値とUI操作](../competitor-evidence/2026-10-27/deep/testrigor-extra-07.png) | official-ui-image | [掲載元](https://support.testrigor.com/support/solutions/articles/154000231623-how-to-do-api-testing-using-testrigor-) |
| [View Execution：step画像・log・出力](../competitor-evidence/2026-10-27/deep/testrigor-extra-08.png) | official-ui-image | [掲載元](https://support.testrigor.com/support/solutions/articles/154000231623-how-to-do-api-testing-using-testrigor-) |

![Suite設定：種類・URL・認証・OS／browser — official-ui-image](../competitor-evidence/2026-10-27/deep/testrigor-extra-01.png)

![Test Cases：custom caseの追加 — official-ui-image](../competitor-evidence/2026-10-27/deep/testrigor-extra-02.png)

![ケース編集：APIの戻り値とUI操作 — official-ui-image](../competitor-evidence/2026-10-27/deep/testrigor-extra-07.png)

## 一次情報

- [公式製品ページ](https://testrigor.com/)
- [APIとUIを結ぶテストの作成・実行](https://support.testrigor.com/support/solutions/articles/154000231623-how-to-do-api-testing-using-testrigor-)
