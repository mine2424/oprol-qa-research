# mabl — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#mabl)

## 調査範囲

Web・モバイル・APIの継続テスト。今回の画面根拠は公式Helpの公開APIから取得した現行記事とUI素材。検索結果の旧説明より記事本文を優先。

比較上の位置：回帰・開発工程の直接比較。追加理由：既存テスト・フロー・要求資料をAgentの文脈に使い、作成・編集・実行・保守まで扱うため。

公式UI画像・紹介映像まで。アカウント内の生成・実行・通知・権限は未操作。初回原稿の「mablは回帰のみ」という扱いを広げた。

## 作業の流れ

Workspace／Build tests → 目的・資料・既存ケース → outlineを修正 → cloud／local生成 → Agents Tasks → 実行結果 → 既存テストの編集・再確認

## 機能の構成

Build tests、Agents > Tasks／Settings、Trainer、テスト詳細（Build history／Plans／Change history等）、環境・連携。全ナビの実アカウント確認ではない。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 入力 | Build tests・Agent chat | 自然言語に加え既存テスト、要求・期待のファイル、接続済みツールのケースを参照する。 |
| 計画 | Outline・Test information | タスク、再利用フロー、検査、参照画像を確認し、会話で計画を直す。 |
| 生成 | Cloud／local authoring | クラウドまたはDesktop App経由のlocal環境で作成。生成しながら動作を確認する説明。 |
| 介入 | Trainer agent mode | 計画・手順を確認し、停止・手動記録・step生成を使い分ける。 |
| 進捗 | Agents > Tasks | 複数セッションの進捗・入力待ちを追い、終わった会話へ戻る。 |
| 結果 | テスト詳細・履歴 | 実行の結果と履歴、関連する計画・変更を参照する。 |
| 保守 | Edit test with agent | 既存テストを選び、変更したいことを会話で伝える。 |
| 連携 | CLI／MCP・外部管理 | 開発Agentから計画・生成・debugを行い、Jira等の期待を文脈に使う。 |

## 人の担当と比較上の着眼点

期待、資料・既存資産の選択、outlineの修正、生成・保守結果のレビュー。

調査者の解釈：資産が増えた組織で、既存のフロー・テスト・要求をどう再利用するかという比較が必要。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

- [開発Agent→対象操作→PR→回帰の紹介表示（公式アニメーション）](../competitor-evidence/2026-10-27/deep/mabl-expanded-walkthrough.mp4)（22.9秒、official-ui-animation）。[公式の掲載元](https://www.mabl.com/)。
  見る場面：[3秒：目的を指定](../competitor-evidence/2026-10-27/deep/mabl-expanded-walkthrough-t003.png)、[10秒：対象の操作](../competitor-evidence/2026-10-27/deep/mabl-expanded-walkthrough-t010.png)、[16秒：PRの確認](../competitor-evidence/2026-10-27/deep/mabl-expanded-walkthrough-t016.png)、[21秒：回帰suiteの結果](../competitor-evidence/2026-10-27/deep/mabl-expanded-walkthrough-t021.png)。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [The New test tab on the Build tests page, with the prompt, the + button, and the Start with mabl button](../competitor-evidence/2026-10-27/deep/mabl-doc-0-0.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/38361400751380-Agentic-test-authoring-for-web-apps) |
| [The + menu below the prompt, with the Existing test, File, Case, and Azure Boards work item options](../competitor-evidence/2026-10-27/deep/mabl-doc-0-1.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/38361400751380-Agentic-test-authoring-for-web-apps) |
| [The generate button](../competitor-evidence/2026-10-27/deep/mabl-doc-1-0.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/50932677869460-Use-agent-mode-in-the-Trainer) |
| [Entering a prompt to generate steps](../competitor-evidence/2026-10-27/deep/mabl-doc-1-1.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/50932677869460-Use-agent-mode-in-the-Trainer) |
| [Show agent activity](../competitor-evidence/2026-10-27/deep/mabl-doc-1-2.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/50932677869460-Use-agent-mode-in-the-Trainer) |
| [Record mode](../competitor-evidence/2026-10-27/deep/mabl-doc-1-3.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/50932677869460-Use-agent-mode-in-the-Trainer) |
| [The Tasks table on the Agents page, with every task listed in one table and its state in the Status column](../competitor-evidence/2026-10-27/deep/mabl-doc-2-0.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/53564732795412-Agent-tasks-and-notifications) |
| [Edit test with mab](../competitor-evidence/2026-10-27/deep/mabl-doc-3-0.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/51702227921044-Edit-an-existing-test-with-the-mabl-agent) |
| [The + menu below the edit prompt, with the Existing test, File, Case, and Azure Boards work item options](../competitor-evidence/2026-10-27/deep/mabl-doc-3-1.png) | official-ui-image | [掲載元](https://help.mabl.com/hc/en-us/articles/51702227921044-Edit-an-existing-test-with-the-mabl-agent) |

![The New test tab on the Build tests page, with the prompt, the + button, and the Start with mabl button — official-ui-image](../competitor-evidence/2026-10-27/deep/mabl-doc-0-0.png)

![The + menu below the prompt, with the Existing test, File, Case, and Azure Boards work item options — official-ui-image](../competitor-evidence/2026-10-27/deep/mabl-doc-0-1.png)

![The generate button — official-ui-image](../competitor-evidence/2026-10-27/deep/mabl-doc-1-0.png)

## 一次情報

- [公式製品ページ](https://www.mabl.com/)
- [Agentic test authoring for web apps](https://help.mabl.com/hc/en-us/articles/38361400751380-Agentic-test-authoring-for-web-apps)
- [Use agent mode in the Trainer](https://help.mabl.com/hc/en-us/articles/50932677869460-Use-agent-mode-in-the-Trainer)
- [Agent tasks and notifications](https://help.mabl.com/hc/en-us/articles/53564732795412-Agent-tasks-and-notifications)
- [Edit an existing test with the mabl agent](https://help.mabl.com/hc/en-us/articles/51702227921044-Edit-an-existing-test-with-the-mabl-agent)
