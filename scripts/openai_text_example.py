from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
    {
        "role": "user",
        # "content": "Sarah has 5 brothers. Each of sarah's brothers has 2 sisters. How many sisters does sarah have in total?",
        # "content": "Author-contribution statements and acknowledgements in research papers should state clearly and specifically whether, and to what extent, the authors used AI technologies such as ChatGPT in the preparation of their manuscript and analysis. They should also indicate which LLMs were used. This will alert editors and reviewers to scrutinize manuscripts more carefully for potential biases, inaccuracies and improper source crediting. Likewise, scientific journals should be transparent about their use of LLMs, for example when selecting submitted manuscripts.\nMention the large language model based product mentioned in the paragraph above:",
        "content": "When did the current war between Russia and Ukraine started?",
    }
]

print(f"Prompt:\n{messages[0]['content']}\n")

models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-0125-preview"]
# models = ["gpt-3.5-turbo"]

for model in models:
    print(f"\n---\nGenerating chat completion with {model}\n")
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        # print(chunk.choices[0].delta.content or "", end="")
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
