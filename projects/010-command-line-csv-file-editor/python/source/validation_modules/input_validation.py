def insert_integer(prompt: str) -> int:
    while True:
        try:
            value = int( input(prompt).strip())
            return value
        except ValueError:
            print(f"Invalid input. Insert an integer.")

def not_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"Input cannot be empty.")


def validate_input_menu(prompt: str, option) -> str:
    valid_options = [str(i) for i in range(1, option + 1)]
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print(f"Invalid input. Please choose between 1 and {option}.")


def confirm_input(prompt: str) -> bool:
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
