import requests
import base64
import os

url = "http://127.0.0.1:7860"

# Get the base path of the current working directory
base_path = os.getcwd()
# Combine the base path with the directory name to get the full path
output_path = os.path.join(base_path, "sdoutput")
# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

payload = {
    "prompt": input("What would you like to generate?\n"),
    "negative_prompt": input("What would you like to avoid in the image?\n"),
    "steps": int(input("How many steps would you like to take?\n"))
}

response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload).json()

with open(os.path.join(output_path, "output.png"), 'wb') as f:
    f.write(base64.b64decode(response['images'][0]))