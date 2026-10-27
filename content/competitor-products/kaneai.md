# KaneAI（TestMu AI） — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#kaneai)

## 調査範囲

旧LambdaTestのKaneAI URLはTestMu AIへredirect。Web・mobileの自然言語QA、Kane CLI、実行基盤との接続を扱う。PR検証のBeta表示を全機能の一般提供と混ぜない。

比較上の位置：要求・作成・実行・保守の直接比較。追加理由：要求資料からのケース、実行前review、操作中の介入、版・環境・修復まで、Oprolの作業範囲に広く重なるため。

公式の製品説明まで。製品UI・操作動画は今回保存できていない。CLI・実device・対象アプリのテスト・版変更・外部送信は未実施。

## 作業の流れ

要求・URL等 → case／plan → review・approve → UI／API等の操作 → pause・手動介入 → analysis → heal差分／版 → schedule／CLI／CI

## 機能の構成

Test generation、authoring、manual interaction、plan approval、pause、triage、versioning、environment、reusable modules、HyperExecute・schedule・analysis。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 入力 | Case Scenario Generation | Jira・PRD・文書・画像等から構造化したケースを作る説明。 |
| 作成 | Natural language・manual interaction | 文章と手動操作の記録から再利用する手順を作る。 |
| 確認 | Plan review・approve | Agentが作った計画を人が修正・承認した後に実行する説明。 |
| 検証 | UI・API・Network等 | 複数の検証対象を同じ流れに結び付ける。個々の適用条件は未実機確認。 |
| 介入 | Pause・triage | 実行中に止め、stepを直す。失敗時に停止・続行・skip等の扱いを決める。 |
| 保守 | Healing・versioning | 変更したstepの差分、版比較、rollbackを案内。 |
| 再利用 | Environment・modules | 環境差分・条件分岐・loop・共通フローを管理する。 |
| 運用 | CLI・schedule・PR | local／headless実行、code出力、実行基盤への接続。PRへの検証はBeta表記。 |

## 人の担当と比較上の着眼点

入力する期待・対象・認証・操作権限と、生成計画・修復差分・結果を人が判断する。

調査者の解釈：「人が計画を承認し、Agentの実行中にも介入でき、変更の版が残る」点を省かず比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

製品内の画面は未収録。公開説明に基づく機能表と、実際のUIを確認できた範囲を分けている。

## 一次情報

- [公式製品ページ](https://www.testmuai.com/kane-ai/)
