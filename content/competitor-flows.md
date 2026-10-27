# 競合プロダクトの機能・導線・画面調査

確認日：2026年10月27日（日本時間）。[既存の市場・価格比較](02-competitors.md)を補完する。

**[画面・動画ギャラリーを開く](competitor-evidence/2026-10-27/gallery.html)** — 製品別に絞り、動画を再生し、設定・作成・実行・結果・保守の画面を比較できる。

## 対象と確認の水準

初回の25サービスに15製品・サービスを追加し、計40件を製品別に整理した。Amikoo製品とMuukTestの代行は別単位。UserTesting・Synthetic UsersはUXの代替／隣接、Browser Useは内製する場合の実行基盤の参考枠とし、直接競合の数へ混ぜない。Autestは引き続き除外する。問い合わせ・予約・登録フォームの画像、一般的なホームのHero、装飾動画は収録対象から外した。製品操作・機能の画面、操作動画、業務図を区別する。

「全体の機能を整理した」と「全機能を操作した」は異なる。公開文書を使って作業の一巡を洗い出し、公開デモ・既存のサンプル・公式の画面と動画で補完した。アカウント内を開けない製品を操作済みとはしない。

- **R 実画面の読取操作**：ログイン済み環境の既存データを閲覧。今回新規実行したとは限らない。
- **S 公開サンプルの操作**：サンプルに限定。TestNeoのみRun liveを1回起動した。UserTestingは調査作成のツアーを操作した。
- **V 公式の画面・動画**：提供者のUI例・操作映像。今回の自社対象での実行結果ではない。
- **D 公開説明・文書**：機能と手順の記述を確認。画面や実動作の確認とは分ける。
- **U 未確認**：情報不足。非対応という意味ではない。

下表は各工程で得られた最も具体的な根拠。VやDは、その工程の全設定が利用可能と実証したものではない。詳細ページの「調査範囲」を併読する。

## 40製品・サービスの機能・導線と画面の到達範囲

| 製品別の詳細 | 準備 | 設計 | 実行 | 結果 | 保守 | 運用・連携 | 保存画像／動画 | 主な作業の循環 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [TestSprite](competitor-products/testsprite.md) | V | V | V | R | D | R | 36画像／1動画 | Workspace → Project作成 → URL・認証・資料 → 探索 → 計画編集 → 生成・実行 → 結果／Agent Action → 修正・再実行 → List／Schedule／PR |
| [QA.tech](competitor-products/qatech.md) | D | V | V | V | D | D | 2画像／1動画 | 相談／アクセス申請 → Project・Application・Environment → データ／接続 → チャットでテスト作成 → 実行／PR検証 → 結果レビュー → Test Planで継続 |
| [Momentic／Mo](competitor-products/momentic.md) | D | V | V | V | V | V | 11画像／1動画 | Mo: 対象・brief → セッション設定 → 並列探索 → 別Agentで再現 → report・triage。回帰: local editor → YAML → local／CI実行 → 結果 |
| [Touchstone](competitor-products/touchstone.md) | D | D | D | D | D | D | 0画像／1動画 | Knowledge Base → Analystで要求 → 人が承認 → ArchitectでJourney → 承認 → Autopilotでテスト → 決定的実行 → 失敗診断／修復提案 → 承認・再実行 |
| [TestNeo](competitor-products/testneo.md) | S | S | S | S | D | D | 12画像／1動画 | Playground: テンプレート／自然言語 → Preview plan → Run live → Timeline・Events → 画像／動画・SDK。製品: PR取込 → 影響分析 → リスク → 検証 → PASS／WARN／BLOCK |
| [Validate.QA](competitor-products/validate.md) | S | S | S | S | S | D | 6画像／0動画 | URL・認証 → Survey／Session → Features → Tests生成・検証 → Suite → Reports → Selector repair → Copilot／Knowledge／Audit → 再調査 |
| [Canary](competitor-products/canary.md) | D | D | V | V | D | D | 1画像／0動画 | Install prompt → stack接続 → working tree／PR → Read → Run → Break → Verify → case file → 修正 → regression |
| [QA Wolf Platform](competitor-products/qawolf.md) | D | D | V | V | D | D | 0画像／0動画 | 対象アプリ → フロー把握・計画 → Agentで作成 → Playwright／Appium → 手動／schedule／deploy → 失敗調査 → バグ報告・保守 |
| [MagicPod本体](competitor-products/magicpod.md) | V | V | D | D | D | D | 3画像／0動画 | 組織・Project → 対象／端末準備 → UI取得・操作記録／Autopilot → 手順編集 → 実行 → 画像・結果 → 共有部品／修復 → CI・通知 |
| [Autify Aximo](competitor-products/autify.md) | V | V | V | V | D | U | 0画像／4動画 | Try Aximo → 対象とscenario → 自然言語で指示 → AI Chat＋対象画面 → 完了 → Summary／Logs → 再確認 |
| [Docket](competitor-products/docket.md) | V | V | V | V | D | U | 0画像／3動画 | 埋込browser → 操作記録 → ステップ編集／AI指示 → group → 実行 → 結果・retries → repair → 継続 |
| [Meticulous](competitor-products/meticulous.md) | D | D | D | V | D | D | 1画像／0動画 | Recorder導入 → 開発・検証環境で操作記録 → CI・PR接続 → セッション選定・再生 → 基準commitとの差分 → 人／Agentが確認 |
| [Autosana](competitor-products/autosana.md) | D | V | V | V | V | V | 0画像／1動画 | Apps → Flows → Suites → Environment・Variables・Hooks → Run／Automation／PR → Issues・動画・Network → Agent修正 → 再実行 |
| [QualGent](competitor-products/qualgent.md) | V | V | V | V | D | D | 3画像／0動画 | 実利用を記録 → 不具合・再現・回帰候補 → DevLoopで開発中に検証 → Enterpriseで人／AIへ分配 → 統合結果 → 次回の知識 |
| [Spur](competitor-products/spur.md) | D | D | D | V | D | D | 1画像／0動画 | 対象・意図 → 専門Agent → 実操作 → finding・根拠 → bug report → 開発工程／MCP → 再確認 |
| [Revyl](competitor-products/revyl.md) | V | V | V | S | D | V | 14画像／2動画 | Build・branch → device／session起動 → 探索・テスト → Atlas → screen／flow → report → IDE Agent → PR検証 |
| [TesterArmy](competitor-products/testerarmy.md) | D | D | D | D | D | D | 0画像／0動画 | 対象URL／mobile → 自然言語テスト → Run → Results → 画像・動画・issue → Memory → PR／schedule／CI → Slack |
| [Swarm](competitor-products/swarm.md) | D | D | D | D | D | D | 0画像／0動画 | New Test → URL・goal・audience → persona数／swarm → Run → persona別経路 → synthesis → judge → tickets → 同じswarmで再検証 |
| [Tookii](competitor-products/tookii.md) | D | D | D | D | D | U | 0画像／0動画 | URL・対象顧客 → 合成ユーザーを生成・編集 → 調査mode → 実行 → session replay → evidence付きfindings → 改善判断 |
| [Uxia](competitor-products/uxia.md) | V | D | D | V | D | D | 4画像／0動画 | Audience → filters／自社資料 → synthetic test → 必要に応じhuman test／interview → heatmap・発話・成功率 → unified report |
| [MagicPod AIテストセンター](competitor-products/magicpod-center.md) | D | D | D | D | D | D | 1画像／0動画 | 相談 → 資料・範囲共有 → AIで観点・設計 → 専門家review → MagicPodに自動化 → 顧客／MagicPod運用 |
| [SHIFT AIテストエージェント](competitor-products/shift.md) | D | D | D | D | D | U | 0画像／0動画 | 問い合わせ → 仕様書等 → AIテスト設計 → 人の統制 → AI実行 → 結果管理 → 個別運用 |
| [AGEST QA for AI駆動開発](competitor-products/agest.md) | D | D | U | U | U | U | 0画像／0動画 | 課題相談 → 対象工程・品質課題 → AI＋QA engineerによる支援 → 工程別成果 → 運用改善 |
| [アットストリーム](competitor-products/atstream.md) | V | V | V | V | D | U | 3画像／1動画 | 設計書 → ケース設計 → RPAシナリオ → 手動記録 → データ違いで再生 → 証跡・判定 → 不具合台帳 → 再テスト |
| [TESTRA](competitor-products/testra.md) | V | V | U | V | D | U | 2画像／0動画 | 仕様書 → テスト条件 → 人がreview → テストモデル → review → テストケース → 実行管理・導入支援 |
| [mabl](competitor-products/mabl.md) | V | V | V | V | V | D | 9画像／1動画 | Workspace／Build tests → 目的・資料・既存ケース → outlineを修正 → cloud／local生成 → Agents Tasks → 実行結果 → 既存テストの編集・再確認 |
| [testRigor](competitor-products/testrigor.md) | V | V | D | V | D | D | 4画像／0動画 | Suite（URL・認証・OS/browser）→ App Descriptionまたはcustom case → 自然言語・API手順 → 実行 → View Execution → 画像・log・録画 → 修正・再実行 |
| [Amikoo（MuukTest）](competitor-products/amikoo.md) | D | V | D | D | D | D | 1画像／0動画 | App・repo・資料 → scopeとcoverage → workerのtrigger・仕事・通知先 → Playwright生成 → PRで実行 → failureの診断 → 修復・再実行／bug登録 |
| [MuukTest Managed QA](competitor-products/muuktest-service.md) | D | D | D | D | D | D | 0画像／0動画 | 担当QAが理解・戦略 → AI探索 → ケースを専門家がreview → Playwright等で自動化 → 並列実行・CI → 証跡と問題 → 継続保守 |
| [Checksum](competitor-products/checksum.md) | D | V | D | V | D | D | 2画像／0動画 | coverage検出 → ケース案 → Playwright生成 → repoへPR → 実行 → triage／recovered → 修復PRをreview → CIで再確認 |
| [TestDriver](competitor-products/testdriver.md) | D | D | D | V | D | D | 7画像／0動画 | GitHub／IDE／MCP → PR内容・目的 → desktop VM → 視覚操作とassertion → replay・network・action log → 生成testのPR → CI・回帰 |
| [Panaya Test Dynamix](competitor-products/panaya.md) | V | V | D | D | D | D | 7画像／0動画 | Requirement／Feature → Testsを作成・link → cycle／business process → 担当者がRun & Document → evidence → defect → 修正確認・Quick Test再利用 |
| [Testsigma／Atto](competitor-products/testsigma.md) | V | V | V | V | D | V | 6画像／0動画 | Commit・story等 → Generate／context → Tests・Coverage・Test Plan → review・accept → Execute／Automate → Scale → Report・Release gate |
| [Katalon True Platform](competitor-products/katalon.md) | V | V | V | V | D | D | 0画像／1動画 | 要求／ticket → Studio・AI作成 → TestOpsでcase・plan → TestCloud／自社runner → 結果・defect・approval → TrueTestの実利用からcoverage更新 |
| [Tricentis Testim](competitor-products/testim.md) | D | D | D | D | D | D | 0画像／0動画 | 対象 → recording／authoring → 検査・再利用部品 → local／cloud実行 → 結果 → locator・手順保守 → CI |
| [UserTesting](competitor-products/usertesting.md) | S | S | D | D | U | D | 5画像／1動画 | 目的・method → AI draft／prewritten → URL・prototype・画像 → tasks・questionsを編集 → audience → 実施 → recordings → AI summaries・共有 |
| [Synthetic Users](competitor-products/synthetic-users.md) | V | V | V | V | D | U | 2画像／1動画 | Audience・pain points → participant数・studyの目的 → interview → participant別回答 → follow-up → report・recommendations |
| [Browser Use](competitor-products/browser-use.md) | D | D | D | D | D | D | 0画像／0動画 | browser／profile・secrets → goal／task → events・live preview → human takeover → 結果／recording・files → script再実行 |
| [KaneAI（TestMu AI）](competitor-products/kaneai.md) | D | D | D | D | D | D | 0画像／0動画 | 要求・URL等 → case／plan → review・approve → UI／API等の操作 → pause・手動介入 → analysis → heal差分／版 → schedule／CLI／CI |
| [BrowserStack AI（Test Management／LCA）](competitor-products/browserstack-ai.md) | V | V | V | V | V | D | 18画像／2動画 | PRD・ticket等 → Ask AI → case生成・承認 → maintenance／dedup → LCAへ自動化 → 実行・証拠 → failure analysis／healing → MCP・次のrun |

画像数には公式のUI素材と業務図を含み、動画からの切り出しは加算していない。数を実機の確認量・品質・網羅率として使わない。

## 追加した15製品・サービスと理由

追加は知名度や機能数のランキングではなく、比較から抜けていた仕事を補うために行った。

| 追加対象 | 比較で補う範囲 |
| --- | --- |
| mabl・testRigor・Testim | 既存テストの再利用、自然言語・記録による作成、回帰・保守 |
| Testsigma／Atto・Katalon | 要求・文脈→計画→review→実行→証跡→release判断の全体 |
| Amikoo・Checksum・TestDriver | coverage不足、PR検証、コードの所有、失敗診断・修復の循環 |
| Panaya Test Dynamix | 要求と業務テスト、担当者の実施・証跡・defect・修正確認 |
| BrowserStack AI・KaneAI | 要求・計画review・探索・自動化・失敗調査・修復の全体 |
| MuukTest Managed QA | 顧客の設計・保守を専門家とAIが引き取る分担 |
| UserTesting・Synthetic Users | 人の観察と合成回答者による調査の違い |
| Browser Use | QA製品を買わず、開発Agentと実行基盤を組み立てる内製代替 |

[候補台帳](competitor-inventory.md)には、元資料の旧候補と追加探索先も残し、今回の40件を網羅的な市場一覧とはしない。

## 画面で先に見るべき比較

| 比較する仕事 | 見る製品と画面 | 読み取れること |
| --- | --- | --- |
| 初回の準備・要求の入力 | TestSpriteのURL・認証・資料、Moのbrief、TouchstoneのKnowledge Base | URL以外に何が必要で、誰が期待を決めるか |
| 観点・計画の確認 | TestSpriteの探索・Coverage、TestNeoのPreview plan、TESTRAの条件・モデル | 生成から実行までに人がどこで判断するか |
| 実行中の理解 | Aximoの対象画面＋AI Chat、Docketのステップ、TestNeoの進捗 | 何が起きていて、どこで止まったかを追えるか |
| 問題の根拠と再現 | Moの再現Agentとレポート、SpurのBug Book、TestSpriteの結果 | 疑いと確定を分け、修正者へ何を渡すか |
| 変更・修復・再実行 | Momenticの修復差分、Validate.QAのSelector Registry、Touchstoneの資料変更 | 期待の変更と操作の修復をどう扱うか |
| 開発工程との往復 | AutosanaのCLI→PR→Agent修正、RevylのAtlas→Cursor、TestSpriteのGitHub | 結果を読んだ後、どこで修正し、どう再確認するか |
| UX調査の理解 | UxiaのAudience→Analytics→Human Sessions→Report、Swarm・Tookiiの人物像と結果 | AIの推定と人の観察を区別できるか |
| 支援を買う場合 | MagicPod AIテストセンター、SHIFT、AGEST、アットストリーム | ツールに加え、人が引き取る設計・準備・判断の範囲 |

## 実際に操作した範囲

TestSpriteは既存の「UAT UX Audit — Demo Store」を閲覧し、Workspace・Project一覧、4ケース、4実行、失敗Runのページマップ／一覧、Environment、Run Behaviorを確認した。過去の結果を今回のテスト結果とは数えない。新規の生成・再実行・修復・外部連携は発行していない。

TestNeoは公開のWeb Smokeを1回実行。完了表示は6passed・0failed・31秒・画像6枚。生成された28秒動画も再生した。これはSauce Demoテンプレートの結果であり、業務要求の網羅や検出精度の評価ではない。

Validate.QAはトップ内のSample dataデモでTests、Reports、API Intelligence、Selector Registry、Copilot、AI Auditを切り替えた。表示される24件の成功、修復、tokens・費用はサンプル値。任意URLの探索は実行していない。

Revylは公開Airbnb AtlasのMap、Journeyのステップ、Screens、Reportを操作した。自社アプリの解析・buildは実行していない。QA.tech・Uxia等の紹介表示と、Momentic・Aximo・Docket等の公式映像は、製品への実行依頼とは区別した。

## 残る内部確認

Touchstoneはメールのゲートで内部ツアーへ未到達。QA.tech、Mo、QA Wolf、MagicPod、Aximo、Docket、Meticulous、Autosana、QualGent、Spur、TesterArmy、Swarm、Tookii、Uxia等は自社対象での実行・保守・権限設定を未操作。国内の相談型サービスは、公開された業務図・対象範囲までで、顧客管理画面全体を確認していない。

旧候補のうちmabl・testRigor・Amikoo／MuukTest・Checksum・TestDriver・Panaya・UserTesting・Synthetic Users・Browser Useを再確認し、Testsigma／Atto・Katalon・Testimも追加した。Quell等の提供状態に留保のあるもの、今回未調査の旧候補・追加候補は[候補台帳](competitor-inventory.md)に残す。採択・買収・終了等の古い記録を現在の商用提供状態へ転記しない。

価格・検出率・顧客価値の順位は本調査では評価していない。観察からOprolの仕様を自動的に変更しない。

## 証跡と出典

[証跡の読み方・一覧](competitor-evidence/2026-10-27/README.md)・[機械可読の出典／hash一覧](competitor-evidence/2026-10-27/manifest.json)。各製品ページに機能表、作業の流れ、人の作業、動画の場面、全画像、一次情報をまとめた。
