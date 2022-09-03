from re import findall
from typing import Callable

from src.config import Replacements, Rules
from src.mutils.check_if_eq import check_if_eq


def format(
        rules: Rules, replacements: Replacements, line: str, words: list[str]
    ) -> str:
    """Formats the text in a line.

    Arguments:
        line -- line that needs to be translated.
        replacements -- math symbols that will be replaced with latex commands.
        words -- list of words in the line split by spaces.
        rules: Rules -- rules that needs to be followed in translation.

    Returns:
        The formatted line.
    """

    rule: str; line_: str; phrase: str; command: str
    rparse: Callable[
            [str, str, str, str], str
        ] = lambda rule, line_, phrase, command: (
            line_.replace(
                    f"{rule}{phrase}{rule}",
                    f"\\{command}{{{phrase}}}"
                )
        )

    inline_maths_: list[str] = findall(rules.inline_math[1], line)
    inline_maths: list[str] = []
    for eq_ in inline_maths_:
        if isinstance(eqs := eq_.split(), list):
            for eq in eqs:
                inline_maths.append(eq)
        else:
            inline_maths.append(eq_)

    inline_maths_.clear()

    for word in words:
        if (quotes := findall(rules.quote[1], line)):
            line = line.replace(
                    f"{rules.quote[0]}{quotes[0]}{rules.quote[0]}",
                    f"``{quotes[0]}''"
                )
        elif (bold := findall(rules.bold[1], line)):
            line = rparse(rules.bold[0], line, bold[0], "textbf")
        elif (italics := findall(rules.italics[1], line)):
            line = rparse(rules.italics[0], line, italics[0], "textit")
        elif (emph := findall(rules.emph[1], line)):
            line = rparse(rules.emph[0], line, emph[0], "emph")
        elif (strike := findall(rules.strike[1], line)):
            line = rparse(rules.strike[0], line, strike[0], "sout")
        elif (supscript := findall(rules.supscript[1], line)):
            line = rparse(
                    rules.supscript[0], line, supscript[0], "textsuperscript"
                )
        elif (subscript := findall(rules.subscript[1], line)):
            line = rparse(
                    rules.subscript[0], line, subscript[0], "textsubscript"
                )
        elif (uline := findall(rules.uline[1], line)):
            line = rparse(rules.uline[0], line, uline[0], "underline")
        elif (link := findall(rules.links, line)):
            line = line.replace(
                    f"[{link[0][0]}]({link[0][1]})",
                    f"\\href{{{link[0][1]}}}{{{link[0][0]}}}"
                )
        elif (icodes := findall(rules.inline_code[1], line)):
            if icodes[0] == "":
                continue
            line = rparse(rules.inline_code[0], line, icodes[0], "texttt")

        if not check_if_eq(rules.inline_math[0], word, inline_maths):
            line = line.replace(word, word.replace("_", r"\_"))

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
                    (
                        "$"
                        +replacements.replacements.get(
                            math_symb, word
                        )
                        +"$"
                    )
                )

    return line.replace("LaTeX", r"\LaTeX{}").replace("%", r"\%")
