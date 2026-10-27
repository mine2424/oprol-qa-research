# TesterArmy — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#testerarmy)

## 調査範囲

自然言語テスト、PRの探索、定期監視、CI・コーディングAgentを同じ結果へ集める。



公開ページの画面例とDocs。自社アプリ実行、production監視、PR接続、Memoryの編集は未操作。

## 作業の流れ

対象URL／mobile → 自然言語テスト → Run → Results → 画像・動画・issue → Memory → PR／schedule／CI → Slack

## 機能の構成

公開紹介にTests / PR Testing / Memory等。Docsに作成・実行・認証・API・連携。実アカウント内ナビは未確認。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 開始 | Start free・Agent prompt | 通常登録と、開発Agentへ渡す入口。 |
| 作成 | Natural language test | ユーザーの流れ・期待を文章で定義する。 |
| 準備 | 認証 | テスト用account・OAuth・OTP等の認証を案内。実際の準備負担は未計測。 |
| 実行 | Web・Mobile | 対象の流れを操作して確認する。 |
| 結果 | Results | 手動・PR・schedule等の結果を同じ一覧へ集めると説明。 |
| 証拠 | Screenshots・recording | 画像・動画付きの問題報告を案内。 |
| 知識 | Memory | 既存のアプリ文脈・確認に使う知識を示す。更新・取消の実挙動は未確認。 |
| 運用 | PR・production monitoring・CI・Slack | PRごとの探索、定期実行、CIジョブ、通知を扱う。 |

## 人の担当と比較上の着眼点

対象と期待、認証準備、誤指摘・結果のレビュー。

調査者の解釈：作成→実行の3段階だけでなく、起動契機が違っても同じResultsへ戻るかを比較する。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

製品内の画面は未収録。公開説明に基づく機能表と、実際のUIを確認できた範囲を分けている。

## 一次情報

- [公式製品ページ](https://tester.army/)
- [pull-request-testing](https://tester.army/platform/pull-request-testing)
- [production-monitoring](https://tester.army/platform/production-monitoring)
- [get-started](https://tester.army/docs/get-started)
