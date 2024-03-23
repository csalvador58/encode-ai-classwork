from typing import Dict, Tuple
from openai import OpenAI
from .utils.func import check_selection, select_chef
import os

# Make sure the OPENAI_API_KEY environment variable is set
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    print(
        '"OPENAI_API_KEY" environment variable is not set. View README.md for more information.'
    )
    exit()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Start of the program

# Define chef personalities here and add more if needed
chef_personalities: Dict[int, Tuple[str, str]] = {
    1: ("Emeril Lagasse", "Let's kick it up a notch!"),
    2: ("Gordon Ramsay", "Bloody hell!"),
}
# Set default chef
selected_chef = 1

print(
    f"\nWelcome, I am {chef_personalities[1][0]}, I'll be your AI chef. {chef_personalities[1][1]}\n"
)

selected_chef = select_chef(chef_personalities)

print(f"\nSelected chef: {chef_personalities[selected_chef][0]}")

exit()





