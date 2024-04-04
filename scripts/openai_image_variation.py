from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# response = client.images.create_variation(
#     image=open("scripts/images/Coconut.png", "rb"),
#     n=1,
#     size="512x512",
# )
response = client.images.edit(
    model="dall-e-2",
    image=open("scripts/images/Coconut.png", "rb"),
    mask=open("scripts/images/Mask.png", "rb"),
    prompt=input("Describe the image you want to generate: "),
    n=1,
    size="512x512",
)

print(f"Variation: {response.data[0].url}")