from re import findall

from src.configs.replacements import Replacements
from src.configs.rules import Rules


def replace_symb(
        line: str,
        word: str,
        rules: Rules,
        replacements: Replacements
    ) -> str:
    """Replace a UTF or ascii string with their respective LaTeX command.

    Args:
        line -- line where there might be a character or string to replace.
        word -- word to match with the string or character in replacement.
        rules -- rules that needs to be followed in translation.
        replacements -- math symbols that will be replaced with latex commands.

    Returns:
        The line with replaced character and strings.
    """

    math_symb: str
    if (
            (
                math_symb := word.replace(
                        rules.inline_math[0], ""
                    )
            ) in replacements.replacements.keys()
        ):
        line = line.replace(
                word,
                replacements.replacements.get(
                    math_symb, word
                )
            )

        if math_symb in findall(rules.inline_math[1], line)[0]:
            line = f"${line}$"

    return line
