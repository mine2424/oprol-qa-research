# 競合・代替・追加候補の台帳

更新：2026年10月27日。[機能・導線比較](competitor-flows.md)・[画面／動画](competitor-evidence/2026-10-27/gallery.html)

最初の26サービスの一覧だけで調査対象を閉じないための台帳。初回25件に追加15件を加え、詳細比較は40件。製品群・サービス・参考基盤を含むため「直接競合40社」「市場を網羅した」とは数えない。Autestは指示により除外する。

「詳細あり」は文書があるという状態で、全機能の実操作済みを意味しない。画像がある製品も、公開素材・操作型ツアー・ログイン後の実画面を区別する。

## 初回の25件

[TestSprite](competitor-products/testsprite.md)、[QA.tech](competitor-products/qatech.md)、[Momentic／Mo](competitor-products/momentic.md)、[Touchstone](competitor-products/touchstone.md)、[TestNeo](competitor-products/testneo.md)、[Validate.QA](competitor-products/validate.md)、[Canary](competitor-products/canary.md)、[QA Wolf Platform](competitor-products/qawolf.md)、[MagicPod本体](competitor-products/magicpod.md)、[Autify Aximo](competitor-products/autify.md)、[Docket](competitor-products/docket.md)、[Meticulous](competitor-products/meticulous.md)、[Autosana](competitor-products/autosana.md)、[QualGent](competitor-products/qualgent.md)、[Spur](competitor-products/spur.md)、[Revyl](competitor-products/revyl.md)、[TesterArmy](competitor-products/testerarmy.md)、[Swarm](competitor-products/swarm.md)、[Tookii](competitor-products/tookii.md)、[Uxia](competitor-products/uxia.md)、[MagicPod AIテストセンター](competitor-products/magicpod-center.md)、[SHIFT AIテストエージェント](competitor-products/shift.md)、[AGEST QA for AI駆動開発](competitor-products/agest.md)、[アットストリーム](competitor-products/atstream.md)、[TESTRA](competitor-products/testra.md)。

## 追加した15件と選定理由

| 比較対象 | 位置付け | 追加する理由 |
| --- | --- | --- |
| [mabl](competitor-products/mabl.md) | 回帰・開発工程の直接比較 | 既存テスト・フロー・要求資料をAgentの文脈に使い、作成・編集・実行・保守まで扱うため。 |
| [testRigor](competitor-products/testrigor.md) | 自然言語テスト・回帰の直接比較 | 自然言語の手順、認証、APIとUIの接続、実行証跡までを同じsuiteで扱うため。 |
| [Amikoo（MuukTest）](competitor-products/amikoo.md) | 探索・PR検証の直接比較 | coverage gapの発見から自社repoのPlaywright生成・修復までが初期顧客の仕事と重なるため。 |
| [MuukTest Managed QA](competitor-products/muuktest-service.md) | 人・AIによる代行の比較 | 顧客に残る設計・保守の作業を引き取る購入理由で重なるため。 |
| [Checksum](competitor-products/checksum.md) | 探索・PR・保守の直接比較 | 検出→生成→失敗の切分け→修復PRまでを明示し、継続QAの責任範囲が広いため。 |
| [TestDriver](competitor-products/testdriver.md) | 開発工程・デスクトップ検証の直接比較 | 実desktop sandboxでPRを確かめ、拡張機能・ネイティブアプリも扱うため。 |
| [Panaya Test Dynamix](competitor-products/panaya.md) | 要求・UAT・証跡管理の比較 | 要求とテスト・担当・証拠・不具合を結び、業務担当が受け入れ確認する工程で重なるため。 |
| [Testsigma／Atto](competitor-products/testsigma.md) | 要求・実行・リリース判断の直接比較 | 要求・既存テスト・coverage・人のaccept・実行・release gateを一巡させるため。 |
| [Katalon True Platform](competitor-products/katalon.md) | テスト運用全体の直接比較 | Studio・TestOps・TestCloud・TrueTestで作成から本番行動の再利用までをつなぐため。 |
| [Tricentis Testim](competitor-products/testim.md) | 回帰自動化・既存QAの比較 | 既存チームが使う記録・安定したUI認識・再利用・CIを代替候補から外さないため。 |
| [UserTesting](competitor-products/usertesting.md) | 人によるUX調査の代替・補完 | AIペルソナだけでなく、人の行動・発話を調べる既存の予算と作業も比較するため。 |
| [Synthetic Users](competitor-products/synthetic-users.md) | 合成ユーザー調査の隣接比較 | Swarm・Tookii等と同じ調査予算で比較され得るが、ブラウザQAとは異なる成果だから。 |
| [Browser Use](competitor-products/browser-use.md) | 実行基盤・内製代替の参考 | 顧客が開発Agentとbrowser基盤を組み合わせて内製する代替手段を把握するため。 |
| [KaneAI（TestMu AI）](competitor-products/kaneai.md) | 要求・作成・実行・保守の直接比較 | 要求資料からのケース、実行前review、操作中の介入、版・環境・修復まで、Oprolの作業範囲に広く重なるため。 |
| [BrowserStack AI（Test Management／LCA）](competitor-products/browserstack-ai.md) | 要求・作成・実行・保守の直接比較 | 既存の要求・手動ケース・環境・結果の基盤にAgentが入り、追加ツールを買わずにQAを進める代替になるため。 |

## 元資料にあり、引き続き確認が必要な候補

以下はユーザー提供資料の第6〜8節に挙がっていた候補を残したもの。分類は元資料の暫定分類で、今回の現行機能・商用提供状態の確認ではない。実機の画像・動画を収録した製品数へ足さない。先に確認する理由も調査者の仮説。

| 候補 | 元資料の分類 | 次に確認する点 |
| --- | --- | --- |
| Quell | 要求・受け入れ | 提供継続と、要求・承認・証跡への実際の対応。Quellの取得失敗を事業終了の証明にしない。 |
| Superflow AI | 要求・受け入れ | 提供継続と、要求・承認・証跡への実際の対応。Quellの取得失敗を事業終了の証明にしない。 |
| Test-Lab.ai | 探索・問題発見 | 同名別製品を避け、公式の現行提供・操作方式・期待の根拠を確認。 |
| SUSATest | 探索・問題発見 | 同名別製品を避け、公式の現行提供・操作方式・期待の根拠を確認。 |
| Orion | 探索・問題発見 | 同名別製品を避け、公式の現行提供・操作方式・期待の根拠を確認。 |
| SanityCheck | 探索・問題発見 | 同名別製品を避け、公式の現行提供・操作方式・期待の根拠を確認。 |
| AnyTest | 探索・問題発見 | 同名別製品を避け、公式の現行提供・操作方式・期待の根拠を確認。 |
| TestOptim AI | 探索・問題発見 | 同名別製品を避け、公式の現行提供・操作方式・期待の根拠を確認。 |
| T-DASH | 回帰・自動化 | 現行の作成・実行・保守の画面、国内顧客の準備負担。 |
| ATgo | 回帰・自動化 | 現行の作成・実行・保守の画面、国内顧客の準備負担。 |
| Synthers AI | AIユーザー・UX | 実ブラウザ操作か画面評価・推定回答か、証拠と認証の方式。 |
| ClickStorm | AIユーザー・UX | 実ブラウザ操作か画面評価・推定回答か、証拠と認証の方式。 |
| FlowLens | AIユーザー・UX | 実ブラウザ操作か画面評価・推定回答か、証拠と認証の方式。 |
| Crowdi | AIユーザー・UX | 実ブラウザ操作か画面評価・推定回答か、証拠と認証の方式。 |
| PersonaIQ | AIユーザー・UX | 実ブラウザ操作か画面評価・推定回答か、証拠と認証の方式。 |
| Mimiq | AIユーザー・UX | 実ブラウザ操作か画面評価・推定回答か、証拠と認証の方式。 |
| Menso | UXの個別候補 | 正式提供・対象フロー・ローカル接続・現行デモ。 |
| Percio | UXの個別候補 | 正式提供・対象フロー・ローカル接続・現行デモ。 |
| Neophyte | UXの個別候補 | 正式提供・対象フロー・ローカル接続・現行デモ。 |
| Jina | 開発工程 | 同名サービスとの同一性、PR検証・操作・報告の範囲。 |
| Releaseworthy | QA代行 | 誰が設計・判断・保守するか、顧客に残る作業、納品資産。 |
| Applause | QA代行 | 誰が設計・判断・保守するか、顧客に残る作業、納品資産。 |
| Autify AI Coworker | QA代行 | 誰が設計・判断・保守するか、顧客に残る作業、納品資産。 |
| STEMS AI（テクバン） | QA代行 | 誰が設計・判断・保守するか、顧客に残る作業、納品資産。 |
| Nioh（bubo） | 要求・設計 | 要求の不足をどう扱うか、実アプリ実行との境界、一般提供の範囲。 |
| Persona AI（シースリーレーヴ） | ユーザー・市場調査 | 合成回答・人の調査・実操作を分け、現在の提供条件を確認。 |
| TOPPANのAIペルソナCX支援 | ユーザー・市場調査 | 合成回答・人の調査・実操作を分け、現在の提供条件を確認。 |
| Idea Echo（日経リサーチ×Relic） | ユーザー・市場調査 | 合成回答・人の調査・実操作を分け、現在の提供条件を確認。 |
| RapiQ | ユーザー・市場調査 | 合成回答・人の調査・実操作を分け、現在の提供条件を確認。 |
| Avenir-UX | 実行基盤・研究 | 研究・OSS・商用品を区別。部品の操作能力をQA精度と数えない。 |
| NTTの仕様・コード・テスト不整合検出技術 | 実行基盤・研究 | 研究・OSS・商用品を区別。部品の操作能力をQA精度と数えない。 |
| Scarlatti／Synthia | 計画・提供状態 | 計画と提供済みの機能を分け、利用可能なデモを確認。 |
| AGEST ZERO TEST | 同社別製品 | 今回調べた同社サービスとの対象・価格・成果物の違い。 |
| MagicPod SiteRover | 同社別製品 | 今回調べた同社サービスとの対象・価格・成果物の違い。 |
| Autify Nexus | 同社別製品 | 今回調べた同社サービスとの対象・価格・成果物の違い。 |
| Octomind | 提供状態に留保 | 終了・残存ページ・現在の新規提供を一次情報で分ける。 |
| Bugster | 提供状態に留保 | 終了・残存ページ・現在の新規提供を一次情報で分ける。 |
| Propolis | 買収記録のある候補 | 独立製品の現行購入先か、統合後の機能か。元資料の買収記録を現状へ転記しない。 |
| Preflight | 買収記録のある候補 | 独立製品の現行購入先か、統合後の機能か。元資料の買収記録を現状へ転記しない。 |
| Hamming AI | 音声・セキュリティの隣接 | 業務Webの機能QAと別の検証対象。拡張範囲を検討する際に確認。 |
| Casco | 音声・セキュリティの隣接 | 業務Webの機能QAと別の検証対象。拡張範囲を検討する際に確認。 |

## 追加探索先

今回の40件に入れていないものも、次の条件で優先順位を見直す。これは未調査の候補一覧であり、現行機能・契約可能性の保証ではない。

| 探索先 | 比較を補う仕事 | 次の確認 |
| --- | --- | --- |
| Tricentis Tosca／qTest | 企業の業務テスト、要求・承認・管理 | Testimとは別単位で、実際の作成・実行・証拠・変更管理を見る |
| Qase／TestRail／Xray | 兼務QAのケース・手動実行・要求・証跡管理 | AI実行ツールを加えず既存管理基盤だけで済む範囲を見る |
| Reflect | 記録・自然言語のWeb回帰 | 現在の提供名・組織・作成と失敗レビューのUIを確認 |
| PlaywrightのAgent・既存の開発Agent＋browser基盤 | 追加SaaSを買わない内製 | 同じ期待・時間・人の作業量で、準備・判定・証拠管理がどこまで残るか |

## 次に掘る基準

1. 初期顧客が同じ確認業務・予算の代替として使うか。
2. URL以外に、要求・期待・認証・データ・人の作業を何が必要か。
3. 作成だけでなく、失敗の診断・修復差分・再実行・次回の保守へ戻れるか。
4. 公開の画面・実行デモ・操作動画に到達できるか。問い合わせフォームの画像では補わない。
5. 提供済み・Alpha／Beta・計画・提供不明を機能単位で分けられるか。

公開情報の不足は非対応の証拠ではない。候補数の多さを調査の深さ・性能の順位として使わない。
