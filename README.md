# Aikimi Neo

**Forge Neoの使い慣れた画面に、追加モデルの導入支援、画像編集、音声付き動画、4K／8K処理、画像の仕上げをまとめたWindows向け派生版です。**

[Stable Diffusion WebUI Forge - Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)を基盤にしています。主な対象はWindows 11・Python 3.13・NVIDIA GPUで、通常起動では自分のPC内だけで利用し、LANやインターネットへ自動公開しません。

[Forge Neoとの違い](#forge-neoとの違い) · [主な機能](#主な機能) · [セットアップ方法](#セットアップ方法) · [その他](#その他)

## Forge Neoとの違い

**Aikimi Neoは、Forge Neoの生成基盤に、本ブランチ独自の仕上げ処理、専用UI、モデル導入支援、操作・効率の改善を加えたものです。** 本リポジトリの既定ブランチ`neo`で提供しています。

機能一覧では、追加した範囲を次の区分で示します。

| 区分 | 意味 |
|---|---|
| **独自追加** | 本ブランチで追加した処理、操作画面、導入・運用支援。 |
| **独自統合** | 外部モデルや実行環境を利用するため、本ブランチで用意した拡張・専用UI・連携処理。 |
| **Forge継承** | 同期基準のForge Neoが備える生成機能やモデル対応。 |

「独自」の対象は、このブランチで追加・改善したソフトウェア部分です。Krea2、Anima、SenseNova、MiniMax H3などのモデル、ComfyUI、基盤ライブラリ、参考技術の出典と利用条件は、それぞれの開発元に従います。各ガイドと[Third-party notices](THIRD_PARTY_NOTICES.md)に参照先を記載しています。

Forge NeoにもKrea2・Animaの基本対応、量子化モデルの読み込み、画像編集・動画生成があります。区分の比較対象は[同期基準時点のForge Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/0d0cb72951b059c8ea17861ba86db8d0f6098c28)です。ベースの情報は[その他](#その他)を参照してください。

## 主な機能

| 機能 | 由来・区分 | できること・本ブランチでの追加部分 | 条件・制約 |
|---|---|---|---|
| **Forge画像生成** | Forge継承 | 通常の`txt2img`、`img2img`、Extras、モデル読み込み。 | モデルごとの条件に従います。 |
| **Krea2 INT8・高解像度処理** | Forge継承＋独自統合 | ForgeのKrea2対応を利用し、モデル導入手順と4K／8K向けの追加処理を同梱。 | 高解像度処理の一部は実験機能。 |
| **Anima 3.8B拡張** | Forge継承＋独自統合 | Qwen3.5を使う拡張、v1.1のSemantic Connector v2対応、INT8変換・導入支援を同梱。 | v1／v1.1に対応。導入する版に合ったモデル構成が必要。 |
| **SenseNova U1.5 Studio** | 独自統合 | テキストからの画像生成、複数画像の編集、別プロセスでの実行を専用画面に統合。 | 対応モデルが必要。24GB Safeは参照2枚・各約512×512、出力2048×2048以下。 |
| **MiniMax H3 Studio** | 独自統合 | ローカルComfyUIと連携する音声付き動画の専用UI。Turbo・INT8 VAE・Fast Decode・Sparse Attentionの任意設定も用意。 | 実行環境とモデルは別途必要。高速化設定には画質・メモリとのトレードオフがあります。 |
| **MiniMax H3 Image** | 独自統合・実験機能 | `H3 Image`タブでテキストからの静止画生成と参照画像による編集。PNGと生成条件を保存。 | 標準H3の最小5フレーム構成を使用。実モデルでのGPU画像生成・画質・速度は未検証です。 |
| **HyperWeave 4K／8K** | 独自追加・実験機能 | 入力画像の構図などを制約にして、読み込み済みの生成モデルで段階的に再作画。 | 細部はモデルによる推定で、入力から変化します。 |
| **Grain Cleaner** | 独自追加 | 微細な粒状感の抑制、細部保護、自動／見本範囲による推定、処理・保護マスク、診断画像、CLI。 | CPU処理・追加モデル不要。初期状態はオフ。 |
| **Color Flatten・色むら確認** | 独自追加 | 色差のムラ補正、Smooth Gradientによる平滑化、色むらの解析・可視化。 | 補正方式に応じた設定を表示。結果を出さない色むら解析は省略。 |
| **Extrasの操作・効率改善** | 独自追加 | 実行順・予定サイズの表示、Grain Cleaner単独設定、画像上の見本範囲選択、解析の再利用、結果要約。 | 見本の画像上選択はSingle Image・Upscaleオフ時。解析キャッシュは直近1画像のみ。 |
| **共通モデル導入CLI** | 独自追加 | Krea2・Anima・SenseNovaの導入、ダウンロード再開、ファイル検証、修復。 | モデル本体はリポジトリに含みません。 |
| **起動プロファイル・公開制限** | 独自追加 | 用途別の起動設定、ローカル限定の既定動作、外部公開時の認証・許可確認。 | 外部公開は明示的な設定が必要。 |
| **Aikimiナビゲーション・Status** | 独自追加 | 追加機能への入口と、ちびあいきみ・実行環境・待機ジョブ・技術詳細の表示。 | 状態表示はKrea2・Anima・SenseNova・MiniMax H3動画の操作中に限定。 |
| **Diagnostics** | 独自追加 | Python・PyTorch・CUDA・GPU・ディスク・モデル・公開状態の診断。 | SettingsとAPIからReady／Warning／Blockedを確認可能。 |

**各モデルを使うには、モデルファイルと実行環境の準備が必要です。** 導入条件は下の機能別ガイド、PC側の準備状況はSettingsのDiagnosticsで確認できます。Grain Cleanerは追加モデルなしで利用可能です。

### 機能別ガイド

- [Anima 3.8B guide](extensions-builtin/anima-3-8b/README.md)
- [SenseNova U1.5 Studio guide](extensions-builtin/sensenova-u15-studio/README.md)
- [MiniMax H3 Studio：動画生成](extensions-builtin/minimax-h3-studio/README.md)
- [MiniMax H3 Image：実験的な静止画生成](extensions-builtin/minimax-h3-studio/IMAGE_GUIDE.md)
- [MiniMax H3の任意の高速化設定](docs/minimax-h3-acceleration.md)
- [HyperWeave guide](extensions-builtin/hyperweave/README.md)
- [Krea2 high-resolution notes](docs/krea2_local_supersample_detail_ja.md)
- [Grain Cleanerガイド](docs/grain-cleaner.md)

<details>
<summary>WebUIの操作と状態表示の詳細</summary>

<a id="webuiの操作境界"></a>

**Extrasの独自追加・改善**は次のとおりです。

- Generate付近に、現在有効な処理の順序と予定サイズを表示。
- **Grain Cleanerだけ実行する設定にする**ボタンで、Upscale・Color Flatten・色むら確認をオフに設定。
- Color Flattenは選択中の方式で使う設定だけ表示し、非表示にした値も保持。
- Grain Cleanerの見本範囲は、プレビュー上の対角2点から選択。拡大と併用する場合やバッチでは、処理後の座標を手入力。
- 同じ画像の強度・細部保護・マスクなどを変えた再実行では、直近1画像の解析を再利用。
- 結果は状態・変更画素率・所要時間を要約し、詳細JSONを展開式で表示。無変更や診断画像省略の理由も明記。

操作方法、キャッシュの更新条件、CLIは[Grain Cleanerガイド](docs/grain-cleaner.md)を参照してください。`H3 Image`は静止画専用の独立タブです。上部の`MiniMax H3`ショートカットは動画の`H3 Studio`を開きます。

通常の`txt2img`、`img2img`、`Extras`、`Settings`に加え、画面上部から追加機能を開けます。

- **Krea2**：画像生成用のPreset`krea`への切り替え。
- **Anima**：Preset`anima`への切り替えと、専用設定欄の表示。
- **SenseNova・MiniMax H3**：それぞれの専用Studioの表示。

Krea2・Animaを選んでも、操作中の`txt2img`／`img2img`タブは維持されます。他のタブから選んだ場合は`txt2img`へ移動します。

追加機能を利用している間は、ちびあいきみが実行状態や待機ジョブを表示します。詳細情報は展開して確認でき、通常のForge画面へ戻ると状態表示も閉じます。

</details>

## セットアップ方法

<a id="quick-start"></a>

### 必要な環境

先に次を用意してください。コマンドはPowerShell 7で実行します。

- Git
- Python 3.13
- PowerShell 7の`pwsh`
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- 対象PyTorch buildに対応したNVIDIA driver

### ダウンロードと起動

```powershell
git clone --branch neo https://github.com/AiWithYou/sd-webui-forge_neo_Aikimi.git
cd sd-webui-forge_neo_Aikimi
.\aikimi-launch.ps1 -Profile LocalSafe
```

`aikimi-launch.bat`をダブルクリックした場合も、`LocalSafe`で起動します。起動後に<http://127.0.0.1:7861>を開いてください。

`LocalSafe`は自分のPC内だけで利用する通常起動です。初回は必要なライブラリを自動導入します。既定のPyTorchは`2.11.0+cu130`、torchvisionは`0.26.0+cu130`なので、対応するNVIDIAドライバーを用意してください。

<a id="model-setup"></a>

### モデルの導入

使いたいモデルのコマンドだけを実行してください。モデル本体・VAE・テキストエンコーダー・LoRAは、このリポジトリとは別に導入します。

| モデル | 導入コマンド |
|---|---|
| Krea2 | `python .\tools\aikimi_setup.py install krea2` |
| Anima 3.8B v1.1 | `python .\tools\aikimi_setup.py install anima38` |
| SenseNova U1.5 | `python .\tools\aikimi_setup.py install sensenova` |

中断したダウンロードは再開でき、取得したファイルも検証します。Animaの変換にはNVIDIA GPUと初回起動で作成される仮想環境が必要なので、先に通常起動を済ませてください。

<details>
<summary>batファイルから導入する場合</summary>

次のファイルを、ダウンロードしたフォルダーから実行する方法も使えます。

```text
download_krea2_int8_convrot_models.bat
download_anima38_v11_int8_convrot_models.bat
download_sensenova_u15_int8.bat
```

Animaを新しく導入する場合は、v1.1用のファイルを選んでください。

</details>

必要な空き容量、導入状況の確認、ファイルの修復は[モデル導入ガイド](docs/model-installation.md)にまとめています。

MiniMax H3の実行環境とモデルの準備は、[MiniMax H3 Studioガイド](extensions-builtin/minimax-h3-studio/README.md)を参照してください。

<a id="起動profile"></a>

### 起動プロファイル

通常は`LocalSafe`を使います。別の設定で起動する場合は、`-Profile`の後を次の表から選んでください。

```powershell
.\aikimi-launch.ps1 -Profile LocalSafe
```

| 起動設定 | 用途 | 接続できる範囲 |
|---|---|---|
| `LocalSafe` | 通常のWebUIとAPI | 自分のPC内 |
| `LocalAPI` | APIだけを起動 | 自分のPC内 |
| `Development` | 開発・画面確認用 | 自分のPC内 |
| `LowVRAM` | GPUメモリが少ない環境向け | 自分のPC内 |
| `RTX3090Recommended` | RTX 3090向け | 自分のPC内 |
| `LANAuthenticated` | 認証付きでLAN内の別端末から利用 | 認証必須。接続範囲はネットワーク設定による |

#### 認証付きLAN利用

`--listen`、loopback以外の`--server-name`、`--share`、`--ngrok`は、`--aikimi-remote`と認証がなければ起動前に失敗します。

`LANAuthenticated`を使う場合は、Git管理外の次の2ファイルを作成してください。

```text
secrets/gradio-auth.txt
secrets/api-auth.txt
```

各行は`username:password`形式です。

```powershell
.\aikimi-launch.ps1 -Profile LANAuthenticated
```

Basic認証だけでインターネットへ直接公開しないでください。TLS reverse proxyとfirewallを併用します。詳しくは[security model](docs/security-model.md)と[SECURITY.md](SECURITY.md)を参照してください。

### `webui-user.bat`のローカル設定

`webui-user.bat`で起動オプションを変更する場合は、設定例をコピーして`webui-user.local.bat`を作成し、そちらを編集してください。この個人用ファイルはGitの管理対象から除外されています。

```powershell
Copy-Item .\webui-user.example.bat .\webui-user.local.bat
```

## その他

### ベース・同期情報

| 項目 | 内容 |
|---|---|
| 既定ブランチ | `neo` |
| ベース | `Haoming02/sd-webui-forge-classic`の`neo` |
| 最終同期基準 | `0d0cb72951b059c8ea17861ba86db8d0f6098c28`（Forge Neo 2.29後の`arch`更新を含む） |
| 取り込み時のマージコミット | `661439ba2b44b78346506c9b2f2178bc39275bff` |
| 主対象 | Windows 11、Python 3.13、NVIDIA GPU |
| コードのライセンス | AGPL-3.0。モデルとアセットには別条件が適用される場合があります。 |

### DiagnosticsとAPI

SettingsのDiagnosticsで、PCやモデルの準備状況を確認できます。状態をAPIから取得する場合は、次の読み取り専用URLを使います。

```text
GET /aikimi/api/v1/health
GET /aikimi/api/v1/status
GET /aikimi/api/v1/capabilities
```

`LocalSafe`での確認例：

```powershell
Invoke-RestMethod http://127.0.0.1:7861/aikimi/api/v1/health
Invoke-RestMethod http://127.0.0.1:7861/aikimi/api/v1/capabilities
```

LANなどの別端末から利用する場合は認証が必要です。認証情報や機密性の高いファイルパスは、APIの応答から除外します。

<a id="update"></a>

### 更新方法

WebUIを終了し、Aikimi NeoをダウンロードしたフォルダーでPowerShellを開いて、次を実行してください。このリポジトリの`neo`ブランチを最新版に更新します。

```powershell
git switch neo
git pull --ff-only origin neo
```

更新が終わったら、`aikimi-launch.bat`をダブルクリックするか、普段使っている起動コマンドでWebUIを起動してください。導入済みのモデルや保存した画像を、ダウンロードし直す必要はありません。

<a id="test"></a>

### 開発・テスト

コードを変更する場合の環境構築とテスト手順は[開発ガイド](CONTRIBUTING.md)を参照してください。

<a id="troubleshooting"></a>

### トラブルシューティング

起動できない、モデルを読み込めない、認証で接続できないといった場合は[トラブルシューティング](docs/troubleshooting.md)を確認してください。SenseNovaとMiniMax H3の対処手順も記載しています。

ログや環境情報を共有する際は、パスワード、個人用のフォルダーパス、プロンプトなどが含まれていないか確認してください。

<a id="documentation"></a>

### ドキュメント

- [Security policy](SECURITY.md)
- [Security model](docs/security-model.md)
- [Architecture](docs/architecture.md)
- [Model installation](docs/model-installation.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Contributing](CONTRIBUTING.md)
- [Release checklist](docs/release-checklist.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)

<a id="licenseと配布条件"></a>

### ライセンスと配布条件

コードのライセンスは[AGPL-3.0](LICENSE)です。個別のライセンスがあるライブラリや素材は、それぞれの条件に従ってください。

モデル・VAE・テキストエンコーダー・LoRAなどの利用条件は各配布元で確認できます。出典と個別のライセンス情報は、各機能のガイドと[Third-party notices](THIRD_PARTY_NOTICES.md)を参照してください。
