from re import findall

from src.config import Rules
from src.mutils.check_if_eq import check_if_eq


def format(rules: Rules, line: str, words: list[str]) -> str:
    """Formats the text in a line.

    Arguments:
        line -- line that needs to be translated.
        words -- list of words in the line split by spaces.
        rules: Rules -- rules that needs to be followed in translation.

    Returns:
        The formatted line.
    """

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
        if (bold := findall(rules.bold[1], line)):
            line = line.replace(
                    f"{rules.bold[0]}{bold[0]}{rules.bold[0]}",
                    f"\\textbf{{{bold[0]}}}"
                )
        elif (italics := findall(rules.italics[1], line)):
            line = line.replace(
                    f"{rules.italics[0]}{italics[0]}{rules.italics[0]}",
                    f"\\textit{{{italics[0]}}}"
                )
        elif (emph := findall(rules.emph[1], line)):
            line = line.replace(
                    f"{rules.emph[0]}{emph[0]}{rules.emph[0]}",
                    f"\\emph{{{emph[0]}}}"
                )
        elif (strike := findall(rules.strike[1], line)):
            line = line.replace(
                    f"{rules.strike[0]}{strike[0]}{rules.strike[0]}",
                    f"\\sout{{{strike[0]}}}"
                )
        elif (supscript := findall(rules.supscript[1], line)):
            line = line.replace(
                    (
                        f"{rules.supscript[0]}"
                        f"{supscript[0]}"
                        f"{rules.supscript[0]}"
                    ),
                    f"\\textsuperscript{{{supscript[0]}}}"
                )
        elif (subscript := findall(rules.subscript[1], line)):
            line = line.replace(
                    (
                        f"{rules.subscript[0]}"
                        f"{subscript[0]}"
                        f"{rules.subscript[0]}"
                    ),
                    f"\\textsubscript{{{subscript[0]}}}"
                )
        elif (uline := findall(rules.uline[1], line)):
            line = line.replace(
                    f"{rules.uline[0]}{uline[0]}{rules.uline[0]}",
                    f"\\underline{{{uline[0]}}}"
                )
        elif (link := findall(rules.links, line)):
            line = line.replace(
                    f"[{link[0][0]}]({link[0][1]})",
                    f"\\href{{{link[0][1]}}}{{{link[0][0]}}}"
                )
        elif (icodes := findall(rules.inline_code[1], line)):
            if icodes[0] == "":
                continue

            line = line.replace(
                    (
                        f"{rules.inline_code[0]}"
                        f"{icodes[0]}"
                        f"{rules.inline_code[0]}"
                    ),
                    f"\\texttt{{{icodes[0]}}}"
                )
        elif (quotes := findall(rules.quote[1], line)):
            line = line.replace(
                    f"{rules.quote[0]}{quotes[0]}{rules.quote[0]}",
                    f"``{quotes[0]}''"
                )

        if not check_if_eq(rules.inline_math[0], word, inline_maths):
            line = line.replace(word, word.replace("_", r"\_"))

    return line.replace("LaTeX", r"\LaTeX{}")
