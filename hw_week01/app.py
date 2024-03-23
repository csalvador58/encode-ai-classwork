from typing import Dict, Tuple
from openai import OpenAI
from .utils.func import init_messages, welcome_message, select_prompt
from .utils.personalities import chef_personalities
from .utils.prompts import prompt_selections
import os

# OpenAI setup
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    print(
        '"OPENAI_API_KEY" environment variable is not set. View README.md for more information.'
    )
    exit()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
model = "gpt-3.5-turbo"

# Set defaults
selected_chef = 1
selected_prompt = 1

# Start program

# Choose a chef personality
selected_chef = welcome_message(chef_personalities)

print(
    f"\nYou have selected {chef_personalities[selected_chef][0]} as your AI chef. {chef_personalities[selected_chef][1]}"
)

# Choose a prompt type
selected_prompt = select_prompt(prompt_selections)

print(f"\nYou have selected to -> {prompt_selections[selected_prompt][0]}.")

# Begin conversation with OpenAI
messages = init_messages(
    selected_chef, selected_prompt, chef_personalities, prompt_selections
)

continue_chat = True
while continue_chat:
    print("\n")
    user_input = input("\n---------\n\nEnter your message:\n\n")
    print("\nAI Chef's response: ")
    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "user",
            "content": "".join(collected_messages),
        }
    )

    response = input("\n\nDo you want to continue chatting? (y/n): ")
    if response.lower() != "y" and response.lower() != "yes":
        change_settings = input(
            "\nWould you like to change your AI Chef or the type of help? (y/n): "
        )
        if change_settings.lower() != "y" and change_settings.lower() != "yes":
            exit_response = input("\nWould you like to leave the program? (y/n): ")
            if exit_response.lower() != "y" and exit_response.lower() != "yes":
                continue_chat = True
            else:
                exit()
        else:
            selected_chef = welcome_message(chef_personalities)
            print(
                f"\nYou have selected {chef_personalities[selected_chef][0]} as your AI chef. {chef_personalities[selected_chef][1]}"
            )
            selected_prompt = select_prompt(prompt_selections)
            print(f"\nYou have selected to -> {prompt_selections[selected_prompt][0]}.")
            messages = init_messages(
                selected_chef, selected_prompt, chef_personalities, prompt_selections
            )
            continue_chat = True
    else:
        continue_chat = True


print("\nThank you for chatting with your AI chef. Have a great day!")

exit()
