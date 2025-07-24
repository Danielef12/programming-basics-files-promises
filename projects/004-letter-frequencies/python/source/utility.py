def confirm_operation(message: str) -> bool:
    response: str = input(message + " (y/n): ").strip().lower()
    if response in ["y", "yes"]:
        return True
    elif response in ["n", "no"]:
        return False
    else:
        print("Enter 'y' for yes or 'n' for no.")
        return confirm_operation(message)
