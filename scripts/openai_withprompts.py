from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
    {
        "role": "user",
        "content": input("Type in your prompt:\n"),
    }
]

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
