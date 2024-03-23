from typing import Dict, Tuple


def check_selection(
    chef_id: any, chef_personalities: Dict[int, Tuple[str, str]]
) -> bool:
    if isinstance(chef_id, int) and chef_id in chef_personalities:
        return True
    print("\nInvalid selection. Please try again.\n\n")
    return False


def select_chef(chef_personalities: Dict[int, Tuple[str, str]]):
    print(
        "If you don't want me as your AI chef, here is a list of other AI chefs to choose from: "
    )
    is_valid_selection = False
    while not is_valid_selection:
        for chef, (name, _) in chef_personalities.items():
            print(f"{chef} - {name}")

        try:
            selected_chef = int(input("\nEnter the number of the chef you want: "))
            is_valid_selection = check_selection(selected_chef, chef_personalities)
        except ValueError:
            is_valid_selection = False
            print("\nInvalid selection. Please try again.\n\n")

    return selected_chef
