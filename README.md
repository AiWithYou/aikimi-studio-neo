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

Forge NeoにもKrea2・Animaの基本対応、量子化モデルの読み込み、画像編集・動画生成があります。区分の比較対象は[同期基準時点のForge Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/0d0cb72951b059c8ea17861ba86db8d0f6098c28)です。上流側の最新機能との比較は、この固定時点から変わる可能性があります。同期情報は[その他](#その他)を参照してください。

## 主な機能

| 機能 | 由来・区分 | できること・本ブランチでの追加部分 | 条件・制約 |
|---|---|---|---|
| **Forge画像生成** | Forge継承 | 通常の`txt2img`、`img2img`、Extras、モデル読み込み。 | モデルごとの条件に従います。 |
| **Krea2 INT8・高解像度処理** | Forge継承＋独自統合 | ForgeのKrea2対応を利用し、モデル導入手順と4K／8K向けの追加処理を同梱。 | 高解像度処理の一部は実験機能。 |
| **Anima 3.8B拡張** | Forge継承＋独自統合 | Qwen3.5を使う拡張、v1.1のSemantic Connector v2対応、INT8変換・導入支援を同梱。 | RTX 3090で約1MPの実測記録があります。 |
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

**タブが表示されていても、モデルや実行環境の導入が完了しているとは限りません。** 実行可否はDiagnosticsまたは`/aikimi/api/v1/capabilities`で確認してください。未計測の最低VRAMや処理時間は掲載せず、実測条件は各ガイドに記載しています。

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

2026-09-07のExtras改善（機能実装コミット[`6344db40`](https://github.com/AiWithYou/sd-webui-forge_neo_Aikimi/commit/6344db40a095435dafc6fb059a832f13809bcb4f)）では、GitHubのCPUテスト1158件、Windowsの選択テスト342件、実WebUIのChromiumテスト2件が失敗なしで終了しました。CPUは43件、Windowsは1件をスキップし、それぞれ既知の失敗扱いが1件あります。

Grain Cleanerの改修前後を1024×1536画像で比較した結果は、補正画像と4種類の診断画像のいずれも全画素で差分0でした。同じ画像で強度だけ変えた再実行は、CPUで約1.97秒から0.66秒になっています。これは1画像での測定例です。対象画像全体の画質評価や、追加したH3静止画モードの実モデル生成を確認した結果には含めません。

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
