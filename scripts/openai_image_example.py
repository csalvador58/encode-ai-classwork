from openai import OpenAI
import os 

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.images.generate(
    model='dall-e-2',
    prompt='a ocean view from Hawaii',
    size='256x256',
    n=1,
)

print(response.data[0].url)