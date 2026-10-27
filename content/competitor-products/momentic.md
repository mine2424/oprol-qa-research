# Momentic／Mo — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#momentic)

## 調査範囲

Moの探索セッションと、MomenticのYAML回帰テストを分けて調べる。Moは稼働アプリを操作し、リポジトリは読取用の文脈。



登録入口まで確認。Moを新規起動していない。物理端末は公式Docs上非対応。OSダイアログや外部デスクトップアプリが必要な経路はblockし得る。

## 作業の流れ

Mo: 対象・brief → セッション設定 → 並列探索 → 別Agentで再現 → report・triage。回帰: local editor → YAML → local／CI実行 → 結果

## 機能の構成

Mo workspace・sessions・reports・triage。別系統にlocal appの手順編集・ライブ対象ブラウザ・Network／Console、環境変数、連携設定。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 開始 | Mo workspace | URLまたはアップロード済みモバイルbuildを対象にする。Webはhosted browser、iOSはsimulator、Androidはemulator。 |
| 準備 | Brief・Environment | 期待、アカウント、データ、禁止操作を記述。環境のBASE_URLや任意の仕様書・planも使う。 |
| 文脈 | Repositories | 選択したコード・差分を読取参照する。Moがcheckoutから対象アプリを起動する方式ではない。 |
| 探索 | Session・parallel agents | 計画・探索・bug bash・再現の担当を分ける。各Agentのブラウザ／端末は独立する。 |
| 結果 | Report・coverage gaps | verified／issues found／blocked、期待と実際、再現手順、未検証範囲を返す。 |
| 確認 | Bug reproducer・triage | 機能不具合は別セッションで独立再現。静的な指摘は画像を根拠にする。 |
| 回帰 | Momentic local app・YAML | 繰り返す確認は別のテスト資産としてリポジトリで管理しlocal・CIで実行する。 |
| 保守・連携 | Editor・Network・GitHub／GitLab／Slack | 手順編集と通信の調査、環境・通知・開発工程の接続を扱う。 |

## 人の担当と比較上の着眼点

briefに業務期待と操作制限を与え、未到達・未再現を含めて結果をレビューする。

調査者の解釈：探索で発見した疑いと再現確認を分ける点、完了報告にcoverage gapsを残す点が、Oprolの判定・証拠設計の比較対象。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

- [Mo：担当Agentへの委任→独立再現→根拠付きレポート（紹介動画の一部）](../competitor-evidence/2026-10-27/deep/momentic-mo-reproduction-report.mp4)（27.1秒、recorded-official-video）。[公式の掲載元](https://www.youtube.com/watch?v=5RMQVtk-ayE)。
  見る場面：[2秒：bug basherへの委任](../competitor-evidence/2026-10-27/deep/momentic-mo-t002.png)、[7秒：独立再現](../competitor-evidence/2026-10-27/deep/momentic-mo-t007.png)、[12秒：再現中の対象](../competitor-evidence/2026-10-27/deep/momentic-mo-t012.png)、[17秒：再現根拠の報告](../competitor-evidence/2026-10-27/deep/momentic-mo-t017.png)、[22秒：reportと画像](../competitor-evidence/2026-10-27/deep/momentic-mo-t022.png)、[26秒：開発側の修正へ](../competitor-evidence/2026-10-27/deep/momentic-mo-t026.png)。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [GitHub integration settings](../competitor-evidence/2026-10-27/deep/momentic-vendor-01.png) | official-ui-image | [掲載元](https://momentic.ai/docs/integrations/github) |
| [Slack integration settings](../competitor-evidence/2026-10-27/deep/momentic-vendor-03.png) | official-ui-image | [掲載元](https://momentic.ai/docs/integrations/slack) |
| [Momentic local app showing a test step list, AI action details, a live browser, and browser context tabs](../competitor-evidence/2026-10-27/deep/momentic-vendor-05.png) | official-ui-image | [掲載元](https://momentic.ai/docs/local-app) |
| [Momentic editor while dragging a While loop between AI actions, with undo and redo controls in the toolbar](../competitor-evidence/2026-10-27/deep/momentic-vendor-06.png) | official-ui-image | [掲載元](https://momentic.ai/docs/local-app) |
| [Momentic Network panel showing request filtering, a request waterfall, headers, response details, and timing tabs](../competitor-evidence/2026-10-27/deep/momentic-vendor-07.png) | official-ui-image | [掲載元](https://momentic.ai/docs/local-app) |
| [Network viewer](../competitor-evidence/2026-10-27/deep/momentic-vendor-08.png) | official-ui-image | [掲載元](https://momentic.ai/docs/platforms/web/request-mocking) |
| [Locator auto-healing diff](../competitor-evidence/2026-10-27/deep/momentic-vendor-09.png) | official-ui-image | [掲載元](https://momentic.ai/docs/reliability/auto-maintenance) |
| [Momentic classification showing Healed and Test authorship labels with reasoning about a transient UI race](../competitor-evidence/2026-10-27/deep/momentic-vendor-10.png) | official-ui-image | [掲載元](https://momentic.ai/docs/reliability/auto-maintenance) |
| [Momentic healed step analysis explaining how triage replaced a transient label check with a durable queue-state check](../competitor-evidence/2026-10-27/deep/momentic-vendor-11.png) | official-ui-image | [掲載元](https://momentic.ai/docs/reliability/auto-maintenance) |
| [A merged Momentic auto-heal pull request with root cause, fix, validation, and links to the base pull request and results](../competitor-evidence/2026-10-27/deep/momentic-vendor-12.png) | official-ui-image | [掲載元](https://momentic.ai/docs/reliability/auto-maintenance) |
| [Runs view](../competitor-evidence/2026-10-27/deep/momentic-vendor-28.png) | official-ui-image | [掲載元](https://momentic.ai/docs/running-tests/results) |

![Momentic local app showing a test step list, AI action details, a live browser, and browser context tabs — official-ui-image](../competitor-evidence/2026-10-27/deep/momentic-vendor-05.png)

![Locator auto-healing diff — official-ui-image](../competitor-evidence/2026-10-27/deep/momentic-vendor-09.png)

![Runs view — official-ui-image](../competitor-evidence/2026-10-27/deep/momentic-vendor-28.png)

## 一次情報

- [公式製品ページ](https://momentic.ai/)
- [Web](https://momentic.ai/docs/quickstart/web)
- [IDE lint](https://momentic.ai/docs/core-concepts/editor-validation)
- [Hosted test environments](https://momentic.ai/docs/running-tests/hosted-test-environments)
- [Variables](https://momentic.ai/docs/core-concepts/variables)
- [JavaScript](https://momentic.ai/docs/integrations/javascript)
- [Authentication](https://momentic.ai/docs/core-concepts/authentication)
- [mo.md](https://momentic.ai/docs/mo)
- [GitHub integration settings](https://momentic.ai/docs/integrations/github)
- [Slack integration settings](https://momentic.ai/docs/integrations/slack)
- [Momentic local app showing a test step list, AI action details, a live browser, and browser context tabs](https://momentic.ai/docs/local-app)
- [Network viewer](https://momentic.ai/docs/platforms/web/request-mocking)
- [Locator auto-healing diff](https://momentic.ai/docs/reliability/auto-maintenance)
- [Runs view](https://momentic.ai/docs/running-tests/results)
