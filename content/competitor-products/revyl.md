# Revyl — 機能・導線・画面

確認日：2026年10月27日。[全体比較](../competitor-flows.md)・[画面／動画ギャラリー](../competitor-evidence/2026-10-27/gallery.html#revyl)

## 調査範囲

モバイルを中心とするビルド・クラウド実行・テスト・Atlas・Agentの作業基盤。DocsにはWeb／computerのalphaもある。



操作したのは公開Atlasサンプル。任意アプリの新規解析・build・CI・Agent起動は未実施。Web等のalphaを一般提供済みとはしない。

## 作業の流れ

Build・branch → device／session起動 → 探索・テスト → Atlas → screen／flow → report → IDE Agent → PR検証

## 機能の構成

Apps / Builds / branches / Sessions / Tests / Workflows / Reports / Atlas（Map・Graph・Screens・Flows）/ Integrations。

下表は公開説明・文書の要約。実操作した範囲は画面一覧と調査範囲に限定し、表全体を実機検証済みとはしない。

| 段階 | 画面・機能 | 入力・操作と次の行動 |
| --- | --- | --- |
| 準備 | Build workspace | buildの状態・logs・起動先を管理する。 |
| 操作 | Cloud device・Session | 動くアプリをbrowser経由で操作・共有する環境を提供する。 |
| 作成 | Tests・YAML・Workflows | 自然言語やYAML等の作成、テスト集合と継続実行を文書化。 |
| 探索 | Atlas exploration | 操作で観測した画面・遷移をアプリマップへ蓄積する。 |
| 参照 | Map・Screens・Flows | 公開Airbnbサンプルのjourney・step・画面・report切替を操作。 |
| 結果 | Report | 動画、Summary、Performance、問題・証拠をまとめる。 |
| 修正 | Cursor・coding agent | 画面やflowの文脈をAgentへ渡す導線を示す。 |
| 継続 | PR・CI・Slack等 | buildと変更の証明・継続テストを開発工程へ返す。 |

## 人の担当と比較上の着眼点

アプリbuild・認証・データの用意、問題判断とAgentへの依頼。

調査者の解釈：実行画面だけでなく、アプリ知識を参照・再利用するAtlasと開発環境の往復が重要。 製品性能の優劣を実証した結論ではない。

## 動画と見る場面

- [Atlasの画面・フローを選択して確認](../competitor-evidence/2026-10-27/deep/revyl-official-01.mp4)（14.8秒、official-product-video）。[公式の掲載元](https://revyl.com/)。
  見る場面：[2秒：Atlasマップ](../competitor-evidence/2026-10-27/deep/revyl-official-01-t002.png)、[5秒：onboarding画面](../competitor-evidence/2026-10-27/deep/revyl-official-01-t005.png)、[9秒：別フロー](../competitor-evidence/2026-10-27/deep/revyl-official-01-t009.png)、[12秒：home画面](../competitor-evidence/2026-10-27/deep/revyl-official-01-t012.png)。
- [公開Atlas：Journey→Screens→Reportの操作](../competitor-evidence/2026-10-27/deep/../revyl-atlas-walkthrough.mp4)（12.6秒、recorded-public-demo）。[公式の掲載元](https://revyl.com/atlas/airbnb/)。

## 画面一覧

| 画面 | 種別 | 出典 |
| --- | --- | --- |
| [A successful cloud build ready to launch on a mobile device](../competitor-evidence/2026-10-27/deep/revyl-vendor-13.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [A coding agent iterating on a mobile game running on a cloud device](../competitor-evidence/2026-10-27/deep/revyl-vendor-14.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [A passed Revyl test report with mobile evidence and performance data](../competitor-evidence/2026-10-27/deep/revyl-vendor-15.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [An Atlas map connecting observed mobile screens and flows](../competitor-evidence/2026-10-27/deep/revyl-vendor-16.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [Revyl opening a Cursor coding agent from an Atlas screen](../competitor-evidence/2026-10-27/deep/revyl-vendor-17.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [test-execution.webp](../competitor-evidence/2026-10-27/deep/revyl-vendor-19.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [pr-validation-result-1600.webp](../competitor-evidence/2026-10-27/deep/revyl-vendor-20.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [release-blocker-1600.webp](../competitor-evidence/2026-10-27/deep/revyl-vendor-21.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [atlas-exploration.webp](../competitor-evidence/2026-10-27/deep/revyl-vendor-22.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [cross-platform-result.webp](../competitor-evidence/2026-10-27/deep/revyl-vendor-23.png) | official-ui-image | [掲載元](https://revyl.com/) |
| [公開Atlas：Map](../competitor-evidence/2026-10-27/deep/../revyl-01-map.png) | public-demo-ui | [掲載元](https://revyl.com/atlas/airbnb/) |
| [公開Atlas：Screens](../competitor-evidence/2026-10-27/deep/../revyl-03-screens.png) | public-demo-ui | [掲載元](https://revyl.com/atlas/airbnb/) |
| [公開Atlas：Report](../competitor-evidence/2026-10-27/deep/../revyl-04-report.png) | public-demo-ui | [掲載元](https://revyl.com/atlas/airbnb/) |
| [公開Atlas：Journey](../competitor-evidence/2026-10-27/deep/../revyl-02-journey.png) | public-demo-ui | [掲載元](https://revyl.com/atlas/airbnb/) |

![A successful cloud build ready to launch on a mobile device — official-ui-image](../competitor-evidence/2026-10-27/deep/revyl-vendor-13.png)

![A coding agent iterating on a mobile game running on a cloud device — official-ui-image](../competitor-evidence/2026-10-27/deep/revyl-vendor-14.png)

![A passed Revyl test report with mobile evidence and performance data — official-ui-image](../competitor-evidence/2026-10-27/deep/revyl-vendor-15.png)

## 一次情報

- [公式製品ページ](https://revyl.com/)
- [llms.txt](https://docs.revyl.com/llms.txt)
