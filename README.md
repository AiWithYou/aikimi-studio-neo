# Aikimi Neo

**Forge Neoの使い慣れた画面に、追加モデルの導入支援、画像編集、音声付き動画、4K／8K処理、画像の仕上げをまとめたWindows向け派生版です。**

[Stable Diffusion WebUI Forge - Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)を基盤にしています。主な対象はWindows 11・Python 3.13・NVIDIA GPUで、通常起動では自分のPC内だけで利用し、LANやインターネットへ自動公開しません。

[Forge Neoとの違い](#forge-neoとの違い) · [主な機能](#主な機能) · [セットアップ方法](#セットアップ方法) · [その他](#その他)

## Forge Neoとの違い

**違いは、モデルの基本対応そのものではなく、追加機能と導入・操作の支援を同梱している点です。** Forge NeoにもKrea2、Anima 3.8B、LoRAの自動変換、量子化モデルの読み込み、画像編集・動画生成の機能があります。以下は、それらを土台にAikimi Neoで追加・統合した内容です。

| 追加・変更点 | Aikimi Neoでできること |
|---|---|
| **Anima 3.8Bの拡張を同梱** | Qwen3.5を使う拡張、v1.1のSemantic Connector v2対応、INT8変換・導入手順をまとめて利用できます。 |
| **画像編集・音声付き動画の専用画面** | SenseNova U1.5 Studioで複数画像を使った編集、MiniMax H3 Studioで音声付き動画を扱えます。対応モデルと実行環境は別途必要です。 |
| **4K／8K向けの追加処理** | Krea2向けの高解像度処理とHyperWeaveを同梱しています。一部は実験機能です。 |
| **画像の粒状感を抑える仕上げ** | ExtrasのGrain Cleanerで、細部を保護しながら微細な粒状感を抑えられます。初期状態はオフです。 |
| **モデル導入を共通化** | Krea2・Anima・SenseNovaを共通コマンドで導入し、中断したダウンロードの再開、ファイル検証、修復を行えます。 |
| **用途別の起動設定と公開制限** | 通常利用・API専用・低VRAM向けなどの起動設定を用意しています。外部公開には明示的な許可と認証を要求します。 |
| **専用ナビゲーションと状態表示** | 通常のForgeタブを保ちつつ、追加機能への入口、ちびあいきみの状態表示、動作環境を確認するDiagnosticsを追加しています。 |

比較対象は[同期基準時点のForge Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/0d0cb72951b059c8ea17861ba86db8d0f6098c28)です。同期情報は[その他](#その他)に記載しています。高速化や画質向上をすべてのモデル・環境で保証するものではありません。

## 主な機能

| 機能 | できること | 補足・制約 |
|---|---|---|
| **Forge画像生成** | 通常の`txt2img`、`img2img`、Extrasを利用。 | Forge Neo由来の機能です。モデルごとの条件に従います。 |
| **Krea2 INT8** | 1024×1024の画像生成と4K／8K向けの処理。 | Forgeの量子化モデル読み込みを利用します。高解像度機能の一部は実験機能です。 |
| **Anima 3.8B** | Qwen3.5を使う画像生成、v1.1のSemantic Connector v2、52層DiT、28／40／52層LoRAへの対応。 | 拡張を同梱しています。RTX 3090で約1MPの実測記録があります。 |
| **SenseNova U1.5** | テキストからの画像生成と複数画像を使った編集。 | 別プロセスで実行します。24GB Safeは参照2枚・各約512×512、出力2048×2048以下です。 |
| **MiniMax H3** | 音声付き動画の生成。 | PC内のComfyUIと連携します。対応する実行環境とモデルが別途必要です。外部有料APIは呼びません。 |
| **HyperWeave** | 候補に制約をかけながら細部を生成する4K／8Kアップスケール。 | 同梱の実験機能です。 |
| **Grain Cleaner** | 細部を保護しながら画像の微細な粒状感を抑制。 | Extrasで有効にします。CPU処理で、追加モデルは不要です。初期状態はオフです。 |
| **Aikimi Status** | ちびあいきみと実行環境・バックエンド・待機ジョブ・技術詳細を表示。 | Krea2・Anima・SenseNova・MiniMax H3の操作中だけ表示します。 |
| **Diagnostics** | Python・PyTorch・CUDA・GPU・ディスク・モデル・公開状態を診断。 | SettingsとAPIからReady／Warning／Blockedを確認できます。 |

**タブが表示されていても、モデルや実行環境の導入が完了しているとは限りません。** 実行可否はDiagnosticsまたは`/aikimi/api/v1/capabilities`で確認してください。未計測の最低VRAMや処理時間は掲載せず、実測条件は各ガイドに記載しています。

### 機能別ガイド

- [Anima 3.8B guide](extensions-builtin/anima-3-8b/README.md)
- [SenseNova U1.5 Studio guide](extensions-builtin/sensenova-u15-studio/README.md)
- [MiniMax H3 Studio guide](extensions-builtin/minimax-h3-studio/README.md)
- [HyperWeave guide](extensions-builtin/hyperweave/README.md)
- [Krea2 high-resolution notes](docs/krea2_local_supersample_detail_ja.md)
- [Grain Cleanerガイド](docs/grain-cleaner.md)

<details>
<summary>WebUIの操作と状態表示の詳細</summary>

<a id="webuiの操作境界"></a>

Extras に **Grain Cleaner / 微細な粒状感を抑制** を追加しました（初期状態はオフ）。細部保護付きの原寸処理、自動／見本範囲の推定、処理・保護マスク、診断画像に対応します。操作方法とCLIは [Grain Cleanerガイド](docs/grain-cleaner.md) を参照してください。

Forge由来の`txt2img`、`img2img`、`Extras`、`Settings`は、Forge Neoのタブ構成とQuick Settingsを維持します。Gradioが所有するタブ列は変更せず、その直前へAikimi専用の細い1行を置き、`Krea2`、`Anima`、`SenseNova`、`MiniMax H3`を直接選べるようにしています。カード型ランチャーや別ダッシュボードは追加しません。

- `Krea2`はUI Presetの`krea`を選択するaliasです。現在のForgeタブが`txt2img`または`img2img`ならそのタブを維持し、別のタブから開いた場合は`txt2img`へ移動します。`Krea2 2-Stage Upscale`は自動選択しません。
- `Anima`はUI Presetの`anima`を選択するaliasです。現在のForgeタブが`txt2img`または`img2img`ならそのタブを維持し、別のタブから開いた場合は`txt2img`へ移動した上で、選択したタブの`Anima 3.8B`設定欄を展開します。
- `SenseNova`と`MiniMax H3`は、専用Studioタブとして直接開きます。

ちびあいきみは、4つのAikimi入口を開いている間だけ操作領域の先頭へ表示され、折りたたみ時は高さ64px以下の状態欄でRuntime、Backend、Queue、進捗、展開可能な技術詳細を示します。通常のForgeタブでは表示と状態取得を停止します。従来の全画面共通ヘッダーと固定オーバーレイは廃止しました。

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

Local Safeは次を有効にします。

- WebUIとAPIを`127.0.0.1`へbind
- Gradio share、ngrok、LAN公開を無効化
- dark theme、BnB、tiled Conv2d、cudaMallocAsync
- `forge_neo_model_paths.yaml`がある場合だけ共有model pathを追加

初回起動は依存関係を導入します。現在のlauncher既定はPyTorch`2.11.0+cu130`とtorchvision`0.26.0+cu130`です。通常は対応NVIDIA driverと、launcherが導入するPyTorch wheelを使います。追加CUDA Toolkitの要否はcustom extensionごとに確認してください。

<a id="model-setup"></a>

### モデルの導入

モデル、VAE、テキストエンコーダー、LoRAはリポジトリに含みません。使いたいモデルの`install`コマンドだけを実行してください。すべてを導入する必要はありません。統一CLIは固定revision、size、SHA-256を検査し、`.part`から再開します。

```powershell
python .\tools\aikimi_setup.py list
python .\tools\aikimi_setup.py install krea2
python .\tools\aikimi_setup.py install anima38
python .\tools\aikimi_setup.py install sensenova
python .\tools\aikimi_setup.py verify
python .\tools\aikimi_setup.py repair anima38 --dry-run
```

`--dry-run`はfilesystemとnetworkを変更しません。`--json`を付けると、相対pathと結果をJSONで返します。現在の固定artifactはpublicで、tokenを必要としません。tokenをcommandやURL queryへ書かないでください。

| profile | 最終配置または一時peak | 注意 |
|---|---:|---|
| Krea2 | 約17.68 GiB | checkpoint、Qwen3-VL、VAE |
| Anima 3.8B v1.1 | v1.1用batの一時peak約17.82 GiB | 共通encoderとVAEも新規導入するCLIは約19.16 GiB |
| SenseNova U1.5 | 最終約17.28 GiB | 既存並列PowerShell installerの一時peakは約33.79 GiB |

表の容量に加えて、ファイルシステムと更新用の空き容量も確保してください。Anima変換にはCUDA device 0と準備済みForge venvが必要です。先に通常起動で依存関係を導入してください。

既存のbatも互換入口として残します。

```text
download_krea2_int8_convrot_models.bat
download_anima38_v11_int8_convrot_models.bat
download_anima38_int8_convrot_models.bat
download_sensenova_u15_int8.bat
```

Animaの旧ファイル名はv1用です。新規導入ではv1.1用batまたは統一CLIを使います。

詳しい固定値、repair、licenseは[Model installation](docs/model-installation.md)を参照してください。

MiniMax H3の実行環境とモデルの準備は、[MiniMax H3 Studioガイド](extensions-builtin/minimax-h3-studio/README.md)を参照してください。

<a id="起動profile"></a>

### 起動プロファイル

通常は`LocalSafe`を使います。必要に応じて、起動時のプロファイルを変更してください。

```powershell
.\aikimi-launch.ps1 -Profile LocalSafe
.\aikimi-launch.ps1 -Profile LocalAPI
.\aikimi-launch.ps1 -Profile Development
.\aikimi-launch.ps1 -Profile LowVRAM
.\aikimi-launch.ps1 -Profile RTX3090Recommended
```

| profile | 用途 | 公開範囲 |
|---|---|---|
| `LocalSafe` | 通常のWebUIとAPI | loopbackのみ |
| `LocalAPI` | APIだけを起動 | loopbackのみ |
| `Development` | UI debug | loopbackのみ |
| `LowVRAM` | 低VRAM向け | loopbackのみ |
| `RTX3090Recommended` | RTX 3090向け既定 | loopbackのみ |
| `LANAuthenticated` | 認証付きLAN利用 | 明示的なremote opt-in |

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

既存更新との互換を保つため、今回のreleaseでは`webui-user.bat`を追跡済みのthin wrapperとして残します。個人設定はGit管理外の`webui-user.local.bat`へ置き、認証値は書かないでください。秘密なしの例からlocal fileを作成できます。

```powershell
Copy-Item .\webui-user.example.bat .\webui-user.local.bat
```

次のmajor releaseでは、移行状況を確認したうえで`webui-user.bat`の追跡解除を検討します。

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

`Settings`のDiagnosticsはlocal checkだけを実行し、model downloadや生成を始めません。read-only APIは次です。

```text
GET /aikimi/api/v1/health
GET /aikimi/api/v1/status
GET /aikimi/api/v1/capabilities
```

Local Safeでの確認例:

```powershell
Invoke-RestMethod http://127.0.0.1:7861/aikimi/api/v1/health
Invoke-RestMethod http://127.0.0.1:7861/aikimi/api/v1/capabilities
```

remote modeでは認証が必要です。APIはtoken、password、認証file path、機密性が高い絶対pathを返しません。

<a id="update"></a>

### 更新方法

通常利用者はAikimi Neoの`neo`をfast-forwardで更新します。

```powershell
git switch neo
git pull --ff-only
```

model、output、secret、`webui-user.local.bat`はGit管理外です。更新前に`git status`を確認し、追跡fileへ書いた個人設定を退避してください。

Forge Neo upstreamとの同期はmaintainer作業です。

```powershell
git remote add upstream https://github.com/Haoming02/sd-webui-forge-classic.git
git fetch upstream neo
```

同期では、Aikimiのsecurity guard、BnB／NF4／GGUF互換、Anima、SenseNova、MiniMax H3、高解像度workflowを個別に検証します。詳しくは[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。

<a id="test"></a>

### テスト

通常のCI相当testは、CPU、offline、外部model downloadなしで動きます。

```powershell
uv pip install --python .\venv\Scripts\python.exe -r tools\requirements-test.txt
.\venv\Scripts\python.exe .\tools\run_ci_tests.py --verbosity 1
```

setup CLIだけを短く確認する場合:

```powershell
.\venv\Scripts\python.exe -m unittest -v tools.tests.test_aikimi_setup
.\venv\Scripts\python.exe -m ruff check tools\aikimi_setup.py tools\tests\test_aikimi_setup.py
.\venv\Scripts\python.exe -m ruff format --check tools\aikimi_setup.py tools\tests\test_aikimi_setup.py
```

CIは用途別に、lint、unit tests、Windows smoke、installer、secret scan、dependency audit、CodeQL、dependency reviewを実行します。GPU live testは通常testと分け、未実施の機能を成功扱いしません。release前の全gateは[Release checklist](docs/release-checklist.md)にあります。

### 既存の動作確認記録

Windows、Python 3.13、Gradio 6.17.3の実WebUIをChromeで開き、Krea2が`txt2img`と`img2img`の現在位置を維持し、他タブからだけ`txt2img`へ戻ることを確認しています。両モードのLora検索、Preset表示、選択中のForgeタブ表示も確認し、ページ由来のconsole errorはありませんでした。

Forge Neo 2.29の取り込みと依存更新では、CPU回帰テストに加え、RTX 3090でKrea2の`txt2img`／`img2img`、Anima 3.8B v1、Anima 3.8B v1.1の実生成まで確認しています。Anima v1.1はPreset条件の512×512、32 steps、ER SDEで、Semantic Connector v2を含む非空の正常画像を確認しました。ここでの結果を、未計測modelの速度や画質へ一般化しません。

<a id="troubleshooting"></a>

### トラブルシューティング

起動、remote auth、CUDA、model setup、SenseNova、MiniMax H3の確認手順は[Troubleshooting](docs/troubleshooting.md)にあります。

logやsysinfoを共有する前に、認証情報、URL query、絶対path、prompt、入力basenameを目視してください。自動redactionだけで安全を保証できません。

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

codeは[AGPL-3.0](LICENSE)です。nested directoryに別licenseがある場合は、そのcopyright noticeと条件を保持します。

model、VAE、text encoder、LoRA、font、画像asset、生成物には別条件が適用される場合があります。特にKrea2、Anima、SenseNova、MiniMax H3の条件は利用時点の配布元で確認してください。

`assets/aikimi`の由来、権利保有者、再配布条件は、監査時点のリポジトリだけでは確認できません。権利を推測して断定せず、第三者向けrelease前にasset noticeを整備します。確認済みの出典と未解決項目は[Third-party notices](THIRD_PARTY_NOTICES.md)に記録しています。
