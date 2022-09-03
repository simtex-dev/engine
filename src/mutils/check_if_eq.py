from re import match, sub


def check_if_eq(rule: str, word: str, references: list[str]) -> bool:
    """Check if the word is an equation based on referece.

    Args:
        word -- the word to be checked.
        references -- set of equations found in the line.

    Returns:
        Whether the word is an equation or not.
    """

    pattern: str = sub(r"\\", r"\\\\", word).replace(rule, '')

    re_char: str
    for re_char in list("*^&$+?{}|()[]"):
        pattern = pattern.replace(re_char, f"\\{re_char}")

    eq: str
    for eq in references:
        if match(f".?|.+{pattern}.?|.+", eq):
            return True

    return False
