# Swarm — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#swarm)

## 調査範囲

AIペルソナによるUX評価。画面評価と実ブラウザの目的達成テストを区別する。



Docsの導線と公開紹介。今回ライブテスト・ログイン後dashboard・ticket送信は未実行。JudgeもAIであり人間の利用者の観察ではない。

## 作業の流れ

New Test → URL・goal・audience → persona数／swarm → Run → persona別経路 → synthesis → judge → tickets → 同じswarmで再検証

## 機能の構成

Dashboard / New Test / Swarms / Results / organization settings / Billing。CLI・MCPにはlocal tunnelの入口。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 開始 | New Test | URL、目的、対象者、Agent数または保存済みswarmを選ぶ。 |
| 人物像 | Personas・Swarms | 生成・手動追加したペルソナ集合を保存して再利用する。 |
| 接続 | Local・Auth | CLIでlocalhostのtunnel、認証付きフローを扱う。 |
| 実行 | Live browser | AIペルソナが目的へ操作。画面のみの評価と枠を分ける。 |
| 個別結果 | Per-persona | 各操作・画像・思考・達成／停止／errorを読む。 |
| 統合 | Synthesis report | 共通の摩擦・良かった点・優先度をまとめる。 |
| 判断補助 | Judge・Tickets | 別AIの判定・confidence・根拠、issue化しやすい記述を返す。 |
| 運用 | Org・Billing・MCP | 共通swarm・結果の共有、役割、課金、外部Agentからの再実行。 |

## 人の担当と比較上の着眼点

対象者・目的を設計し、AI所見の妥当性を人の調査や事実と照合する。

調査者の解釈：ペルソナ別の証拠と総合報告を往復できるか、同じ人物像で改善前後を比較できるかを見る。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

製品操作を確認できる動画を今回保存できていない。存在しない・非対応という意味ではない。問い合わせ画面で代用しない。

## 画面一覧

製品内の画面は未収録。公開説明に基づく機能表と、実際のUIを確認できた範囲を分けている。

## 一次情報

- [公式製品ページ](https://www.useswarm.co/)
- [Dashboard](https://docs.useswarm.co/getting-started/dashboard)
- [Quickstart](https://docs.useswarm.co/getting-started/quickstart)
- [Personas & Swarms](https://docs.useswarm.co/concepts/personas)
- [Test Results](https://docs.useswarm.co/concepts/test-results)
- [Testing Local Apps](https://docs.useswarm.co/guides/local-testing)
