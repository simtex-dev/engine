def prompt(
        msg: str, assume_yes: bool, other_cases: bool = False
    ) -> bool | str:
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
        ans: bool | str
        if (
                ans := input(f"\033[1mINPT\033[0m\t {msg}").lower().strip()
            ) == "y":
            if not other_cases:
                return True
            else:
                return ans

    return False
