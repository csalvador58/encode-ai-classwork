from typing import Dict, Tuple, Union

Option = Union[Dict[int, Tuple[str, str]], Dict[int, Tuple[str, list]]]


def check_selection(id: any, option: Option) -> bool:
    if isinstance(id, int) and id in option:
        return True
    print("\nInvalid selection. Please try again.\n")
    return False


def select_chef(chef_personalities: Dict[int, Tuple[str, str, list]]) -> int:
    print(
        "If you want to select another AI chef, here is a list to choose from:\n"
    )
    is_valid_selection = False
    while not is_valid_selection:
        for chef, (name, _, _) in chef_personalities.items():
            print(f"{chef} - {name}")

        try:
            selected_chef = int(input("\nEnter the number of the chef you want to chat with: "))
            is_valid_selection = check_selection(selected_chef, chef_personalities)
        except ValueError:
            is_valid_selection = False
            print("\nInvalid selection. Please try again.\n")

    return selected_chef


def welcome_message(chef_personalities: Dict[int, Tuple[str, str]]) -> int:

    # Check if user wants to select a different chef
    print(f"\nWelcome, I am {chef_personalities[1][0]}, I'll be your AI chef.\n")
    selected_chef = select_chef(chef_personalities)
    return selected_chef


def select_prompt(prompt_selections: Dict[int, Tuple[str, list]]) -> int:
    print("\n---------\n\nWhat would you like your chef to help with today?\n")

    is_valid_selection = False
    while not is_valid_selection:
        for prompt, (message, _) in prompt_selections.items():
            print(f"{prompt} - {message}")

        try:
            selected_prompt = int(input("\nEnter the number would like to receive help with: "))
            is_valid_selection = check_selection(selected_prompt, prompt_selections)
        except ValueError:
            is_valid_selection = False
            print("\nInvalid selection. Please try again.\n")

    return selected_prompt

def init_messages(selected_chef: int, selected_prompt: int, chef_personalities: Dict[int, Tuple[str, str, list]], prompt_selections: Dict[int, Tuple[str, list]]) -> list:
    init_prompt_type = prompt_selections[selected_prompt][1]
    init_chef_type = chef_personalities[selected_chef][2]
    messages = [*init_prompt_type, *init_chef_type]
    return messages