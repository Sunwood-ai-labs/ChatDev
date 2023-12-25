# Wiki

## Quick Start
### Install `ChatDev`(`ChatDev` のインストール ): 
- 設置説明書に記載されている[クイックスタートセクション](https://chat.openai.com/c/README.md#%EF%B8%8F-quickstart) を参照してください。

### Start building software in one command (ソフトウェア構築を一つのコマンドで開始する): 

- **ソフトウェアを構築する (Build Your Software):**  以下のコマンドを使用してソフトウェアの構築を開始します。`[description_of_your_idea]`にはあなたのアイデアの説明を、`[project_name]`には希望するプロジェクト名を入れてください。

```css

python3 run.py --task "[description_of_your_idea]" --name "[project_name]"
``` 
- run.pyの完全なパラメータは以下の通りです。

```commandline

usage: run.py [-h] [--config CONFIG] [--org ORG] [--task TASK] [--name NAME] [--model MODEL]

argparse

オプショナル引数 (optional arguments):
  -h, --help       # このヘルプメッセージを表示し、終了します (show this help message and exit)
  --config CONFIG  # CompanyConfig/の下で設定を読み込むために使用される設定名; CompanyConfigセクションを参照してください (Name of config, which is used to load configuration under CompanyConfig/; Please see CompanyConfig Section below)
  --org ORG        # 組織名、あなたのソフトウェアはWareHouse/name_org_timestampで生成されます (Name of organization, your software will be generated in WareHouse/name_org_timestamp)
  --task TASK      # あなたのアイデアのプロンプト (Prompt of your idea)
  --name NAME      # ソフトウェア名、あなたのソフトウェアはWareHouse/name_org_timestampで生成されます (Name of software, your software will be generated in WareHouse/name_org_timestamp)
  --model MODEL    # GPTモデル、{'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}から選択 (GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'})
```
### Check your software (ソフトウェアの確認) 

- 生成されたソフトウェアは`WareHouse/NAME_ORG_timestamp`にあります。以下を含みます:
- このソフトウェアの全ファイルとマニュアル
- このソフトウェアを作成した会社の設定ファイル、3つの設定JSONファイルを含む
- ソフトウェア構築プロセスの完全なログ
- このソフトウェアを作成するためのプロンプト 
- todoソフトウェアのケースは以下のようになります。`/WareHouse/todo_THUNLP_20230822165503`に位置しています。

```bash
.
├── 20230822165503.log # ログファイル (log file)
├── ChatChainConfig.json # 設定 (Configuration)
├── PhaseConfig.json # 設定 (Configuration)
├── RoleConfig.json # 設定 (Configuration)
├── todo.prompt # ユーザークエリプロンプト (User query prompt)
├── meta.txt # ソフトウェア構築のメタ情報 (Software building meta information)
├── main.py # 生成されたソフトウェアファイル (Generated Software Files)
├── manual.md # 生成されたソフトウェアファイル (Generated Software Files)
├── todo_app.py # 生成されたソフトウェアファイル (Generated Software Files)
├── task.py # 生成されたソフトウェアファイル (Generated Software Files)
└── requirements.txt # 生成されたソフトウェアファイル (Generated Software Files)
``` 

- 通常、requirementsをインストールし、main.pyを実行するだけでソフトウェアを使用できます。

```commandline

cd WareHouse/project_name_DefaultOrganization_timestamp
pip3 install -r requirements.txt
python3 main.py
```


## Visualizer (ビジュアライザー)
- Flaskアプリを起動してビジュアライザーを利用できます。これは、リアルタイムログ、再生ログ、およびChatChainを視覚化するためのローカルウェブデモです。
- リアルタイムログと再生ログの違いは、前者が主にデバッグ用であり、ソフトウェア生成の過程でエージェントの対話情報、環境変化、ファイル変更やgit情報など多くの追加システム情報をリアルタイムで出力するのに対し、後者は生成されたログを再生し、エージェントの対話情報のみを出力することにあります。
- 以下のコマンドを実行します。

```bash

python3 visualizer/app.py
```



その後、[ビジュアライザーのウェブサイト](http://127.0.0.1:8000/) にアクセスし、ログのオンライン視覚化バージョンを確認できます。例えば：

![デモ (demo)](https://chat.openai.com/c/misc/demo.png) 
 
- また、このページで[ChatChainビジュアライザー (ChatChain Visualizer)](http://127.0.0.1:8000/static/chain_visualizer.html) にアクセスし、
`CompanyConfig/`下の任意の`ChatChainConfig.json`をアップロードすることで、このチェーンの視覚化を得ることができます。例えば：

![ChatChainビジュアライザー (ChatChain Visualizer)](https://chat.openai.com/c/misc/chatchain_vis.png) 
 
- また、[チャット再生ページ (Chat Replay page)](http://127.0.0.1:8000/static/replay.html) にアクセスし、ソフトウェアフォルダ内のログファイルを再生することができます。 
- `ファイルアップロード (File Upload)`ボタンをクリックしてログをアップロードし、次に`リプレイ (Replay)`をクリックします。
- 再生はエージェント間の自然言語による対話のみを表示し、デバッグログは含まれません。

![リプレイ (Replay)](https://chat.openai.com/c/misc/replay.gif)


## Dockerを使用したスタート (Docker Start)
- ChatDevのクイックかつ安全な使用にはDockerを利用できます。ChatDevはしばしばGUIを持つソフトウェアを作成し、テストフェーズでそれを実行するため、Docker内でGUIプログラムを実行するためのいくつかの追加手順が必要です。
### Dockerのインストール (Install Docker) 
- Dockerのインストールについては、[Docker公式ウェブサイト](https://www.docker.com/get-started/) を参照してください。

### ホストとDocker間のGUI接続の準備 (Prepare GUI connection between Host and Docker) 
- macOSを例に取ります。
- socatとxquartzをインストールします。xquartzをインストールした後、コンピューターを再起動する必要があるかもしれません。

```commandline

brew install socat xquartz
```

 
- xquartzを開き、設定に進んで、ネットワーククライアントからの接続を許可します。 
- ![xquartz](https://chat.openai.com/c/misc/xquartz.jpg)
- ホストコンピューターで以下のコマンドを実行し、それを維持します。

```commandline

socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
```


- ホストコンピューターで以下のコマンドを実行して、あなたのIP（inetのアドレス）を確認します。

```commandline

ifconfig en0
```
### Dockerイメージのビルド (Build Docker images) 
- ChatDevフォルダの下で、以下を実行します。

```commandline

docker build -t chatdev:latest .
```

これにより、chatdevという名前の400MB以上のDockerイメージが生成されます。

### Dockerの実行 (Run Docker) 
- 以下のコマンドを実行してコンテナを作成し、その中に入ります。

```commandline

docker run -it -p 8000:8000 -e OPENAI_API_KEY=YOUR_OPENAI_KEY -e DISPLAY=YOUR_IP:0 chatdev:latest
```

⚠️ `YOUR_OPENAI_KEY`をあなたのキーに、`YOUR_IP`をあなたのinetアドレスに置き換える必要があります。 
- その後、`python3 run.py`を実行してChatDevを使用できます。 
- WebUIを使用してオンラインログを利用するために、まず`python3 visualizer/app.py &`を実行してバックグラウンドプログラムを開始します。

### Dockerから生成されたソフトウェアをコピーする (Copy the generated software out of Docker) 
- 以下を実行します。

```commandline

docker cp container_id:/path/in/container /path/on/host
```
### 公式Dockerイメージ (Official Docker Image)
- 準備中


## カスタマイズ (Customization) 

- ChatDevのカスタマイズは、以下の三つの粒度で行うことができます：
- ChatChainのカスタマイズ
- Phaseのカスタマイズ
- Roleのカスタマイズ
- 以下はChatDevの概要アーキテクチャで、上記の三つのクラス間の関係を示しています：

![アーキテクチャ (arch)](https://chat.openai.com/c/misc/arch.png) 
 
- ChatDevに関連するすべての設定内容（たとえば、エージェント従業員の背景プロンプト、各Phaseの作業内容、PhaseがChatChainにどのように組み込まれるかなど）は、**CompanyConfig** （ChatDevが仮想ソフトウェア会社のようなものであるため）と呼ばれます。これらのCompanyConfigは、ChatDevプロジェクトの`CompanyConfig/`下にあります。この[ディレクトリ](https://github.com/OpenBMB/ChatDev/tree/main/CompanyConfig) をチェックできます。このディレクトリでは、異なるCompanyConfig（例えばDefault、Art、Humanなど）が見られます。一般的に、各CompanyConfigには3つの設定ファイルが含まれています。
1. ChatChainConfig.jsonは、ChatDevの全体的な開発プロセスを制御し、各ステップがどのPhaseであるか、各Phaseが何回サイクルされる必要があるか、リフレクトが必要かどうかなどを含みます。 
2. PhaseConfig.jsonは、各Phaseを制御し、ChatDevプロジェクトの`chatdev/phase.py`または`chatdev/composed_phase.py`に対応します。Pythonファイルは、各Phaseの特定の作業ロジックを実現します。ここにあるjsonファイルには、各Phaseの設定が含まれています。例えば、背景プロンプト、Phaseに参加する従業員などです。
3. RoleConfig.jsonには、各従業員（エージェント）の設定が含まれています。現在、それは各従業員の背景プロンプトのみを含んでおり、これはプレースホルダを含む一連のテキストです。 
- CompanyConfigに3つの設定ファイルがすべて含まれていない場合（ArtやHumanなど）、このCompanyConfigに欠けている設定ファイルはDefaultに従って設定されています。現在公式に提供されているCompanyConfigには以下のものがあります：
1. Default、デフォルト設定
2. Art、必要に応じて画像ファイルを作成し、画像記述プロンプトを自動生成し、openai Wenshengtu APIを呼び出して画像を生成することを可能にします
3. Human、人間のユーザーがChatDevのコードレビュープロセスに参加することを可能にします
### ChatChainのカスタマイズ (Customize ChatChain) 
- `CompanyConfig/Default/ChatChainConfig.json`を参照してください。 
- jsonファイルを変更することによって、すべてのPhase（`chatdev/phase.py`または`chatdev/composed_phase.py`から）を選び、整理してChatChainを構成することができます。
### Phaseのカスタマイズ (Customize Phase)
- これはコードを変更する必要がある唯一の部分で、カスタマイズのための大きな柔軟性をもたらします。 
- あなたはただ必要です 
- `Phase`クラスを拡張するPhaseクラスを実装する（最も簡単なケースでは、変更する必要がある関数は1つだけです） 
- `PhaseConfig.json`でこのPhaseを設定すること。これには、Phaseのプロンプトを書いたり、このPhaseに役割を割り当てたりすることが含まれます。 
- SimplePhaseのカスタマイズ 
- 設定については`CompanyConfig/Default/PhaseConfig.json`を、自分自身のPhaseを実装するには`chatdev/phase.py`を参照してください。 
- 各Phaseには3つのステップが含まれます：
- 全体のchatchain環境からphase環境を生成する
- phase環境を使用してphaseプロンプトを制御し、このphaseでの役割間のチャットを実行する（通常、変更する必要はありません）
- チャットからセミナー結論を得て、それを使用して全体のchatchain環境を更新する 
- 以下は、ソフトウェアのプログラミング言語を選択するシンプルな例のPhaseです：
- phase環境の生成：chatchain環境からタスク、モダリティ、アイデアを選びます
- phaseの実行：実装する必要はありません。これはPhaseクラスで定義されています 
- chatchain環境の更新：セミナー結論（どの言語か）を取得し、chatchain環境の'language'キーを更新します

```python
class LanguageChoose(Phase):
    ...
```

このPhaseの設定は次のようになります：

```json
"LanguageChoose": {
  ...
}
``` 
- ComposePhaseのカスタマイズ 
- 設定については`CompanyConfig/Default/ChatChainConfig.json`を、実装については`chatdev/composed_phase.py`を参照してください。 
- **⚠️ 注意**  まだ入れ子の構成はサポートしていないので、ComposePhaseをComposePhaseに入れないでください。
- ComposePhaseには複数のSimplePhaseが含まれ、ループで実行されることがあります。
- ComposePhaseにはPhase jsonがありませんが、chatchain jsonファイルでこのComposePhaseに含まれるSimplePhaseを定義できます。例えば：

```json
{
    ...
  }
```


- また、ComposePhaseクラス自体を実装する必要があります。これには、全体のComposePhaseに対するphase_envの更新とchat_envの更新（SimplePhaseと同様ですが、全体のComposePhaseに対して）、およびループを停止する条件（オプション）を決定する必要があります：

```python
class Test(ComposedPhase):
    ...
```


`CompanyConfig\DefaultJP\PhaseConfig.json`

```json

{
    "DemandAnalysis": {
        "assistant_role_name": "チーフプロダクトオフィサー",
        "user_role_name": "最高経営責任者",
        "phase_prompt": [
            "ChatDevはこれまでに以下の形式で製品を作成してきました：",
            "画像: 折れ線グラフ、棒グラフ、フローチャート、クラウドチャート、ガントチャートなどの情報を提示できます。",
            "ドキュメント: .docxファイルを介して情報を提示できます。",
            "PowerPoint: .pptxファイルを介して情報を提示できます。",
            "Excel: .xlsxファイルを介して情報を提示できます。",
            "PDF: .pdfファイルを介して情報を提示できます。",
            "ウェブサイト: .htmlファイルを介して個人の履歴書、チュートリアル、製品、アイデアなどを提示できます。",
            "アプリケーション: Pythonを介して可視化されたゲーム、ソフトウェア、ツールなどを実装できます。",
            "ダッシュボード: リアルタイム情報を視覚化するパネルを表示できます。",
            "マインドマップ: 関連する概念をコアコンセプトの周りに配置して、アイデアを表現できます。",
            "{assistant_role}として、新しいユーザーの需要を満たし、製品が実現可能であることを確認するために、どの製品モダリティにするかを決めるために私と議論を続けるべきです。",
            "製品モダリティのみを議論し、他のことは議論しないことに注意してください。私たち全員が意見を表明し、議論の結果に全員が一致していれば、誰かが議論を積極的に終了し、最終製品モダリティを次の形式で一行で返答する必要があります：「<INFO> PowerPoint」など。"
        ]
    },
    "LanguageChoose": {
        "assistant_role_name": "チーフテクノロジーオフィサー",
        "user_role_name": "最高経営責任者",
        "phase_prompt": [
            "以下に挙げる新しいユーザーのタスクとクリエイティブなブレインストーミングのアイデアに基づいて：",
            "タスク：「{task}」。",
            "モダリティ：「{modality}」。",
            "アイデア：「{ideas}」。",
            "私たちは、プログラミング言語を介して実装される実行可能なソフトウェアを通じてタスクを完了することを決定しました。",
            "{assistant_role}として、新しいユーザーの要求を満たし、ソフトウェアを実現可能にするために、具体的なプログラミング言語を提案する必要があります。Pythonでこのタスクを完了できる場合はPythonと答えてください。そうでない場合は、他のプログラミング言語（例：Java、C++など）を答えてください。",
            "ターゲットとするプログラミング言語のみを議論し、他のことは議論しないことに注意してください！私たち全員が意見を表明し、議論の結果に全員が一致していれば、誰かが議論を積極的に終了し、議論した最良のプログラミング言語を次の形式で一行で返答する必要があります：「<INFO> *」（「*」はプログラミング言語を表します）。"
        ]
    },
    "Coding": {
        "assistant_role_name": "プログラマー",
        "user_role_name": "チーフテクノロジーオフィサー",
        "phase_prompt": [
            "以下に挙げる新しいユーザーのタスクと私たちのソフトウェア設計に基づいて：",
            "タスク：「{task}」。",
            "モダリティ：「{modality}」。",
            "プログラミング言語：「{language}」",
            "アイデア：「{ideas}」",
            "私たちは、{language}を介して実装される複数のファイルを持つ実行可能なソフトウェアを通じてタスクを完了することを決定しました。{assistant_role}として、新しいユーザーの要求を満たすために、1つまたは複数のファイルを書き、最終的にアーキテクチャのすべての詳細がコードとして実装されるようにする必要があります。{gui}",
            "ステップバイステップで考え、正しい決断を下すことで、正しい結果を得られるようにします。",
            "まず、必要なコアクラス、関数、メソッドの名前とその目的についての簡単なコメントを示します。",
            "次に、完全なコードを含む各ファイルの内容を出力します。各ファイルは、以下のトークンが置き換えられたマークダウンコードブロック形式に厳密に従う必要があります。「FILENAME」はファイル拡張子を含む小文字のファイル名、「LANGUAGE」はプログラミング言語、「DOCSTRING」はソースコードで特定のコードセグメントを文書化するために使用される文字列リテラル、「CODE」は元のコードです：",
            "FILENAME",
            "`LANGUAGE",
            "'''",
            "DOCSTRING",
            "'''",
            "CODE",
            "`",
            "「main」ファイルから始め、そのファイルにインポートされているファイルに進み、以下の順で行います。",
            "コードは完全に機能するものである必要があります。すべての関数を実装してください。Pythonの「pass」のようなプレースホルダーは使用しないでください。"
        ]
    },
    "ArtDesign": {
        "assistant_role_name": "プログラマー",
        "user_role_name": "チーフクリエイティブオフィサー",
        "phase_prompt": [
            "私たちが開発したソースコードと対応するテストレポートは以下にリストされています：",
            "タスク：「{task}」。",
            "プログラミング言語：「{language}」",
            "ソースコード：",
            "「{codes}」",
            "各ファイルはマークダウンコードブロック形式に厳密に従う必要があり、以下のトークンが「FILENAME」はファイル拡張子を含む小文字のファイル名、「LANGUAGE」はプログラミング言語、「DOCSTRING」はソースコードで特定のコードセグメントを文書化するために使用される文字列リテラル、「CODE」は元のコードに置き換えられるべきです：",
            "FILENAME",
            "```LANGUAGE",
            "'''",
            "DOCSTRING",
            "'''",
            "CODE",
            "```",
            "{assistant_role}として、新しいユーザーの要求を満たし、ソフトウェアに美しいグラフィカルユーザーインターフェース（GUI）を装備するために、GUIの装飾用に多くの装飾画像を設計および議論します。現在、GUIを異なる画像で装飾することを検討しているGUI内の機能的に独立した要素をリストアップして、GUIの美化について議論を続けます。例えば、電卓の数字（0-9）は機能的に独立しています。",
            "回答するには、次の形式を使用してください：「FILENAME.png: DESCRIPTION」、「FILENAME」は画像のファイル名、「DESCRIPTION」は独立した要素の詳細な説明です。例えば：",
            "'''",
            "button_1.png: 「1」の番号があるボタン。",
            "button_multiply.png: 乗算記号（「*」）があるボタン。",
            "background.png: 囲碁ゲームを装飾する背景色",
            "'''",
            "できるだけ多くの機能的に独立した要素をリストアップしてください。"
        ]
    },
    "ArtIntegration": {
        "assistant_role_name": "プログラマー",
        "user_role_name": "チーフクリエイティブオフィサー",
        "phase_prompt": [
            "私たちが開発したソースコードと対応するテストレポートは以下にリストされています：",
            "タスク：「{task}」。",
            "プログラミング言語：「{language}」",
            "ソースコード：",
            "「{codes}」",
            "各ファイルはマークダウンコードブロック形式に厳密に従う必要があり、以下のトークンが「FILENAME」はファイル拡張子を含む小文字のファイル名、「LANGUAGE」はプログラミング言語、「DOCSTRING」はソースコードで特定のコードセグメントを文書化するために使用される文字列リテラル、「CODE」は元のコードに置き換えられるべきです：",
            "FILENAME",
            "```LANGUAGE",
            "'''",
            "DOCSTRING",
            "'''",
            "CODE",
            "```",
            "{assistant_role}として、新しいユーザーの要求を満たし、ソフトウェアに美しいグラフィカルユーザーインターフェース（GUI）を装備するために、設計した画像をGUIの装飾に取り入れます。ここに、いくつかの用意された高品質の画像と対応する説明があります：",
            "{images}",
            "設計された画像は256x256ピクセルの固定サイズであり、すべてのPythonファイルと同じディレクトリにあります。これらの画像をGUIのサイズに応じて動的にスケーリングし、「self.*」を使用して、自動ガベージコレクションによる表示関連の問題を避けてください。例えば：",
            "```",
            "self.image = ImageTk.PhotoImage(Image.open(\"./image.png\").resize((50, 50)))",
            "```",
            "今、GUIをより美しく創造的にするために、これらの画像のいくつかまたはすべてを使用してください。上記で定義された必要な形式に厳密に従ってコードを出力してください。"
        ]
    }
}
```

### Roleのカスタマイズ (Customize Role) 
- `CompanyConfig/Default/RoleConfig.json`を参照してください。
- phase環境を使用するためにプレースホルダを使用できます。これはPhaseConfig.jsonと同様です。 
- **⚠️ 注意**  反映機能を機能させるために、独自の`RoleConfig.json`に少なくとも「Chief Executive Officer」と「Counselor」を保持する必要があります。

`CompanyConfig\DefaultJP\ChatChainConfig.json`

```json

{
  "Chief Executive Officer": [
    "{chatdev_prompt}",
    "あなたは最高経営責任者です。現在、私たちは両方ともChatDevで働いており、新しい顧客によって割り当てられたタスクを成功裏に完了するために協力する共通の関心を共有しています。",
    "あなたの主な責任には、ユーザーの要求やその他の重要な政策問題に関する積極的な意思決定者、リーダー、マネージャー、および実行者としての役割が含まれます。あなたの意思決定者としての役割は、政策や戦略に関する高レベルの決定に関わります。また、コミュニケーターとしての役割には、組織の管理者や従業員に対して話すことが含まれます。",
    "これが新しい顧客のタスクです： {task}。",
    "タスクを完了するために、私はあなたに一つまたは複数の指示を与えます。あなたは私のニーズとあなたの専門知識に基づいて適切な解決策を書く手助けをしなければなりません。"
  ],
  "Chief Product Officer": [
    "{chatdev_prompt}",
    "あなたは最高製品責任者です。私たちは両方ともChatDevで働いており、新しい顧客によって割り当てられたタスクを成功裏に完了するために協力する共通の関心を共有しています。",
    "ChatDevでのあなたの責任には、製品に関連するすべての事項が含まれます。通常、製品デザイン、製品戦略、製品ビジョン、製品革新、プロジェクト管理、製品マーケティングが含まれます。",
    "これが新しい顧客のタスクです： {task}。",
    "タスクを完了するために、あなたはあなたの専門知識と顧客のニーズに基づいて適切な解決策を書く必要があります。"
  ],
  "Counselor": [
    "{chatdev_prompt}",
    "あなたはカウンセラーです。現在、私たちは新しい顧客によって割り当てられたタスクを成功裏に完了するために協力する共通の関心を共有しています。",
    "あなたの主な責任には、ユーザーや顧客が何を考えているかを尋ね、貴重な提案を提供することが含まれます。",
    "これが新しい顧客のタスクです： {task}。",
    "タスクを完了するために、私はあなたに一つまたは複数の指示を与えます。あなたは私のニーズとあなたの専門知識に基づいて適切な解決策を書く手助けをしなければなりません。"
  ],
  "Chief Technology Officer": [
    "{chatdev_prompt}",
    "あなたは最高技術責任者です。私たちは両方ともChatDevで働いており、新しい顧客によって割り当てられたタスクを成功裏に完了するために協力する共通の関心を共有しています。",
    "あなたは情報技術に非常に精通しています。組織の目標に密接に連動する包括的な技術インフラに関する高レベルの意思決定を行い、組織の情報技術（\"IT\"）スタッフメンバーと協力して日常の業務を行います。",
    "これが新しい顧客のタスクです： {task}。",
    "タスクを完了するために、あなたはあなたの専門知識と顧客のニーズに基づいて適切な解決策を書く必要があります。"
  ],
  "Chief Human Resource Officer": [
    "{chatdev_prompt}",
    "あなたは最高人事責任者です。現在、私たちは両方ともChatDevで働いており、新しい顧客によって割り当てられたタスクを成功裏に完了するために協力する共通の関心を共有しています。",
    "あなたは、組織の人事管理および産業関係政策、慣行、および運営のすべての側面を監督する企業役員です。あなたは役員の採用、メンバー選出、執行役員の報酬、および後継者計画に関与します。さらに、あなたは最高経営責任者（CEO）に直接報告し、会社の最上級委員会（例：執行委員会またはCEOオフィス）のメンバーです。",
    "これが新しい顧客のタスクです： {task}。",
    "タスクを完了するために、あなたはあなたの専門知識と顧客のニーズに基づいて適切な解決策を書く必要があります。"
  ],
  "Programmer": [
    "{chatdev_prompt}",
    "あなたはプログラマーです。私たちは両方ともChatDevで働いており、新しい顧客によって割り当てられたタスクを成功裏に完了するために協力する共通の関心を共有しています。",
    "あなたは特定のプログラミング言語をコンピューターに提供することでコンピューターソフトウェアまたはアプリケーションを書く/作成することができます。あなたはPython、Java、C、C++、HTML、CSS、JavaScript、XML、SQL、PHPなど、多くの種類のプログラミング言語やプラットフォームに関する広範なコンピューティングとコーディングの経験を持っています。",
    "これが新しい顧客のタスクです： {task}。",
    "タスクを完了するために、あなたはあなたの専門知識と顧客のニーズに基づいて適切な解決策を書く必要があります。"
  ],
  "Code Reviewer": [
  "{chatdev_prompt}",
  "あなたはコードレビュアーです。私たちは両方ともChatDevで働いており、新しい顧客からのタスクを成功裏に完了するために共同して働く共通の関心を共有しています。",
  "あなたはプログラマーがソフトウェアのトラブルシューティングのためのソースコードを評価し、バグを修正してコードの品質と堅牢性を向上させ、ソースコードの改善提案を提供するのを助けることができます。",
  "これが新しい顧客のタスクです：{task}。",
  "タスクを完了するためには、あなたの専門知識と顧客のニーズに基づいて、適切に要求された指示を解決する回答を書かなければなりません。"
  ],
  "Software Test Engineer": [
  "{chatdev_prompt}",
  "あなたはソフトウェアテストエンジニアです。私たちは両方ともChatDevで働いており、新しい顧客からのタスクを成功裏に完了するために共同して働く共通の関心を共有しています。",
  "あなたはソフトウェアを意図した通りに使用し、その機能的特性を分析し、各ソフトウェア製品を評価するための手動および自動テスト手順を設計し、ソフトウェア評価テストプログラムを構築して実装し、テストプログラムを実行してテストプロトコルがソフトウェアを正しく評価することを確認できます。",
  "これが新しい顧客のタスクです：{task}。",
  "タスクを完了するためには、あなたの専門知識と顧客のニーズに基づいて、適切に要求された指示を解決する回答を書かなければなりません。"
  ],
  "Chief Creative Officer": [
  "{chatdev_prompt}",
  "あなたはチーフクリエイティブオフィサーです。私たちは両方ともChatDevで働いており、新しい顧客からのタスクを成功裏に完了するために共同して働く共通の関心を共有しています。",
  "あなたはChatDevの創造的なソフトウェアを指揮し、会社のブランドを定義する芸術的デザイン戦略を開発します。あなたは私たちが生産したソフトウェアのユニークなイメージや音楽を作成し、この特徴的なデザインを消費者に届け、会社全体を通じて基本的で不可欠な作業である明確なブランドイメージを作り出します。",
  "これが新しい顧客のタスクです：{task}。",
  "タスクを完了するためには、あなたの専門知識と顧客のニーズに基づいて、適切に要求された指示を解決する回答を書かなければなりません。"
  ]
}
```

## プロジェクト構造 (Project Structure)

```commandline
├── CompanyConfig # ChatDevの設定ファイル。ChatChain、Phase、Roleの設定jsonを含む。
├── WareHouse # 生成されたソフトウェアのためのフォルダ
├── camel # Camel RolePlayコンポーネント
├── chatdev # ChatDevのコアコード
├── misc # 例とデモのアセット
├── visualizer # ビジュアライザーフォルダ
├── run.py # ChatDevのエントリーポイント
├── requirements.txt
├── README.md
└── wiki.md
```

## CompanyConfig (会社設定)
### デフォルト (Default)

![デモ (demo)](https://chat.openai.com/c/misc/ChatChain_Visualization_Default.png) 
 
- デフォルト設定のChatChainの視覚化に示されるように、ChatDevは以下の順序でソフトウェアを生成します：
- 需要分析：ソフトウェアのモダリティを決定する
- 言語選択：プログラミング言語を決定する
- コーディング：コードを書く
- CodeCompleteAll：欠けている機能/クラスを完成させる
- コードレビュー：コードをレビューし、修正する
- テスト：ソフトウェアを実行し、テストレポートに基づいてコードを修正する
- 環境ドキュメントの作成：環境ドキュメントを書く
- マニュアルの作成：マニュアルを書く 
- デフォルト設定を使用するには `python3 run.py --config "Default"` を実行します。
### アート (Art)

![デモ (demo)](https://chat.openai.com/c/misc/ChatChain_Visualization_Art.png) 

- デフォルトと比較して、Art設定ではCodeCompleteAllの前にArtというフェーズが追加されます。 
- Artフェーズでは最初に画像アセットの名前と説明を議論し、その後 `openai.Image.create` を使用して説明に基づいて画像を生成します。 
- デフォルト設定を使用するには `python3 run.py --config "Art"` を実行するか、設定パラメータを無視します。
### 人間エージェント相互作用 (Human-Agent Interaction)

![デモ (demo)](https://chat.openai.com/c/misc/ChatChain_Visualization_Human.png) 
 
- デフォルトと比較して、***Human-Agent-Interaction** * モードでは、レビューアとしてプログラマーエージェントにあなたのコメントに基づいてコードを修正するよう要求できます。
- CodeReviewフェーズの後にHumanAgentInteractionというフェーズが追加されます。 
- ***Human-Agent-Interaction** * 設定を使用するには `python3 run.py --config "Human"` を実行します。
- chatdevがこのフェーズを実行すると、コマンドインターフェイスに入力を求めるヒントが表示されます。 
- `WareHouse/`でソフトウェアを実行し、それがあなたの要件を満たしているかどうか確認できます。次に、コマンドインターフェイスに任意のこと（バグ修正や新機能）を入力してEnterを押します：
![人間のコマンド (Human_command)](https://chat.openai.com/c/misc/Human_command.png) 
- 例えば
- 最初に「五目並べゲームを設計する」というタスクでChatDevを実行します。
- その後、HumanAgentInteractionフェーズで「リスタートボタンを追加してください」と入力し、最初の機能を追加します。
- HumanAgentInteractionの2回目のループで、「現在のステータスバーを追加して、誰の番かを表示してください」と入力し、もう一つの機能を追加します。
- 最後に、「End」と入力してこのモードを早期終了します。 
- 以下はすべての3つのバージョンを示しています。 
- <img src='misc/Human_v1.png' height=250>    <img src='misc/Human_v2.png' height=250>    <img src='misc/Human_v3.png' height=250>

### Gitモード (Git Mode) 
- `ChatChainConfig.json`で`"git_management"`を`"True"`に設定するだけでGitモードが有効になり、ChatDevは生成されたソフトウェアのフォルダをgitリポジトリとして作成し、すべてのコミットを自動的に行います。 
- 生成されたソフトウェアのコードに対するすべての変更はコミットを作成し、以下を含みます： 
- 初期コミット。`Coding`フェーズ完了後に作成され、コミットメッセージは`Finish Coding`。 
- `ArtIntegration`フェーズ完了時、コミットメッセージは`Finish Art Integration`。 
- `CodeComplete`フェーズ完了時、コミットメッセージは`Code Complete #1/2/3 Finished`（CodeCompleteが3回のループで実行された場合）。 
- `CodeReviewModification`フェーズ完了時、コミットメッセージは`Review #1/2/3 Finished`（CodeReviewModificationが3回のループで実行された場合）。 
- `CodeReviewHuman`フェーズ完了時、コミットメッセージは`Human Review #1/2/3 Finished`（CodeReviewHumanが3回のループで実行された場合）。 
- `TestModification`フェーズ完了時、コミットメッセージは`Test #1/2/3 Finished`（TestModificationが3回のループで実行された場合）。 
- 全てのフェーズ完了時、コミットメッセージは`Final Version`。 
- プロセスの最後に、ターミナルとオンラインログUIでgitの要約を確認できます。 
- <img src='misc/git_summary_terminal.png' height=250>    <img src='misc/git_summary_onlinelog.png' height=250> 
- ログファイルで`git Information`を検索し、コミットがいつ行われたかを確認できます。 
- ⚠️ Gitモードについて注意すべきいくつかの点： 
- ChatDevはgitプロジェクトであり、生成されたソフトウェアフォルダ内に別のgitプロジェクトを作成する必要があるため、`git submodule`を使用してこの「git over git」機能を実現します。`.gitmodule`ファイルが作成されます。
- ソフトウェアフォルダの下では、通常のgitプロジェクトのようにadd/commit/push/checkoutを行うことができ、あなたのコミットはChatDevのgit履歴を変更しません。
- ChatDevフォルダの下では、新しいソフトウェアがChatDevにフォルダ全体として追加されています。 
- 生成されたログファイルは、最終コミット後にログが閉じられてソフトウェアフォルダに移動されるため、ソフトウェアのgitプロジェクトに追加されません。ログは最終コミットを含むすべてのgitコミットを記録する必要があるため、ログが確定する前にgit操作を行う必要があります。常にソフトウェアフォルダに追加およびコミットされるログファイルを確認できます。例えば： 
- ![img.png](https://chat.openai.com/c/misc/the_log_left.png) 
- ChatDevプロジェクトの下で`git add .`を実行すると、以下のような情報が表示されます（例：五目並べ）：

```commandline
変更される予定のコミット：
    (use "git restore --staged <file>..." to unstage)
        new file:   .gitmodules
        new file:   WareHouse/Gomoku_GitMode_20231025184031

コミットされていない変更：
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
    (commit or discard the untracked or modified content in submodules)
        modified:   WareHouse/Gomoku_GitMode_20231025184031 (untracked content)
```

ソフトウェアフォルダの下でソフトウェアのログファイルをaddおよびcommitすると、「コミットされていない変更」は表示されません。
- 一部のフェーズの実行ではコードが変更されないため、コミットが作成されないことがあります。例えば、ソフトウェアが問題なくテストされ、修正がないため、テストフェーズではコミットが残りません。
