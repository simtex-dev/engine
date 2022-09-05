def prompt(msg: str, assume_yes: bool, other_cases: bool = False) -> bool:
    """Prompt for user input.

    Args:
        msg -- msg to prompt.
        assume_yes -- whether to assume yes or not.

    Returns:
        Whether the user agreed or otherwise.
    """

    if assume_yes:
        if other_cases:
            return "y"
        return True
    else:
        ans: str
        if (ans := input(f"\033[1mINPT\033[0m\t {msg}").lower() == "y"):
            return True
        else:
            if other_cases:
                return ans.lower()

    return False
