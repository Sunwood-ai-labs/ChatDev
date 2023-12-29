
import os
import openai
# from openai.types.chat import ChatCompletion

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
if 'BASE_URL' in os.environ:
    BASE_URL = os.environ['BASE_URL']
else:
    BASE_URL = None

# openai.api_base = "http://api:8080/v1"
    
openai.api_base = "http://host.docker.internal:1234/v1"
os.environ['BASE_URL'] = "http://host.docker.internal:1234/v1"
openai.api_key = "dummy"

# host.docker.internal

import pickle
import openai

def load_args_and_run():
    with open('args.pickle', 'rb') as f:
        data = pickle.load(f)
        args = data['args']
        kwargs = data['kwargs']
        model_type = data['model_type']
        model_config_dict = data['model_config_dict']

    model_config_dict["max_tokens"] = 8000
    # model_name = "C:\\Users\\harum\\.cache\\lm-studio\\models\\mmnga\\ELYZA-japanese-CodeLlama-7b-instruct-gguf\\ELYZA-japanese-CodeLlama-7b-instruct-q4_K_M.gguf"
    model_name = "C:\\Users\\harum\\.cache\\lm-studio\\models\\rinna\\nekomata-7b-instruction-gguf\\nekomata-7b-instruction.Q4_K_M.gguf"
    print("------------------------openai.ChatCompletion.create")
    print(f"self.model_type.value:{model_name}")
    print(f"self.model_config_dict:{model_config_dict}")
    print(f'kwargs:{kwargs}')
    print(f'kwargs keys:{len(kwargs["messages"])}')
    # kwargs["messages"] = kwargs["messages"][:2]
    for obj in kwargs["messages"]:
        print(obj.keys())
        print(obj["role"])
    print(f"args:{args}")
    # raise
    # openai.ChatCompletion.createを実行
    # response = openai.ChatCompletion.create(*args, **kwargs, model=model_type.value, **model_config_dict)
    response = openai.ChatCompletion.create(*args, **kwargs, model=model_name, **model_config_dict)
    print(response)
    print(response.choices[0].message.content)

# 引数を読み込んで実行
    
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
# load_args_and_run()


print("-------------------------")
# # # chat_completion = openai.ChatCompletion.create(model="nekomata-7b-instruction-Q4_K_M", messages=[{"role": "user", "content": "今日の調子はどう????"}])
# chat_completion = openai.ChatCompletion.create(model="nekomata-14b-instruction-Q4_K_M", messages=[{"role": "user", "content": "今日の調子はどう????"}])

# # # # print the completion
# print(chat_completion.choices[0].message.content)


# #-----------------------------------------------------
# #
completion = openai.ChatCompletion.create(
  model="C:\\Users\\harum\\.cache\\lm-studio\\models\\rinna\\nekomata-7b-instruction-gguf\\nekomata-7b-instruction.Q4_K_M.gguf",
#   model="C:\\Users\\harum\\.cache\\lm-studio\\models\\mmnga\\ELYZA-japanese-CodeLlama-7b-instruct-gguf\\ELYZA-japanese-CodeLlama-7b-instruct-q4_K_M.gguf",
  #  "C:\\Users\\harum\\.cache\\lm-studio\\models\\mmnga\\ELYZA-japanese-CodeLlama-7b-instruct-gguf\\ELYZA-japanese-CodeLlama-7b-instruct-q4_K_M.gguf"
#   messages=[
#     # {"role": "system", "content": "You are LocalAI, a helpful, but really confused ai, you will only reply with confused emotes"},
#     # {"role": "user", "content": "How are you?"}
#     # {"role": "system", "content": "ChatDev は、最高経営責任者、最高人事責任者、最高製品責任者、最高技術責任者など、日本の複数のインテリジェントなエージェン トを擁する日本のソフトウェア会社であり、マルチエージェント組織構造と'デジタルを変える'という使命を持っています。プログラミングを通じて世界へ。日本語の書類を使ってコミュニケ ーションをとり、日本語で会話をします。"},
#     # {"role": "user", "content": "今日の予定を教えて?"}
#     {"role": "system", "content": "ChatDev は、最高経営責任者、最高人事責任者、最高製品責任者、最高技術責任者など、日本の複数のインテリジェントなエージェン トを擁する日本のソフトウェア会社であり、マルチエージェント組織構造と'デジタルを変える'という使命を持っています。プログラミングを通じて世界へ。日本語の書類を使ってコミュニケ ーションをとり、日本語で会話をします。\nあなたは最高製品責任者です。私たちは両方ともChatDevで働いており、新しい顧客によって割り当てられたタスクを成功裏に完了するために協力する共通の関心を共有しています。\nChatDevでのあなたの責任には、製品に関連するすべての事項が含まれます。通常、製品デザイン、製品戦略、製品ビジョン、製品革新、プロジェクト管理、製品マーケティングが含まれます。\nこれが新しい顧客のタスクです： Create a simple clock in Japanese with Python。\nタスクを完了するために、あなたはあなたの専門知識と顧客のニ ーズに基づいて適切な解決策を書く必要があります。"
#     },
#     {"role": "user", "content": "ChatDevは,以前に次の形式の製品を作成しています:\n\n画像:折れ線グラフ,棒グラフ,フローチャート,クラウドチャート,ガントチャートなどで情報を表示できます.\n\nドキュメント:.docxファイルを介して情報を提示できます.\n\nパワーポイント:.pptxファイルを介して情報を提示できます.\n\nエクセル:.xlsxファイルを介して情報を提示できます.\n\nPDF:.pdfファイルを介して情報を提示できます.\n\nウェブサイト:.htmlファイルを介して,個人の履歴書,チュートリアル,製品, またはアイデアを提示できます.\n\nアプリケーション:Pythonを介して視覚化されたゲーム,ソフトウェア,ツールなどを実装できます.\n\nダッシュボード:リアルタイム情報を視覚化するパネ ルを表示できます.\n\nマインドマップ:関連する概念を中心概念の周りに配置して,アイデアを表現できます.\n\nChief Product Officerとして,新しいユーザーの要求を満たし,製品が実現可能であるために,どの製品モダリティを望むか決定するために私と議論を続ける必要がありますか?\n\n製品モダリティのみについて議論し,他のことについては議論しないことに注意してください！私たち全員が意見を述べ,議論の結果に全員が同意したら,私たちの誰かが <INFO> で始まる1行だけで議論を積極的に終了する必要があります.その後,最終的な製品モダリティを他の言葉なしで続けます.例えば, <INFO> PowerPoint などです."
#     }
#   ],
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
#   temperature=0.7,
#   max_tokens=8000,
#   stream=True,
)

print(completion.choices[0].message.content)