from re import findall

from src.config import Rules


def appearance(line: str, words: list[str], rules: Rules) -> str:
    """Formats the text in a line.

    Arguments:
    line: str -- line that needs to be translated.
    wc: int -- the number of words in line.
    rules: Rules -- rules that needs to be followed in translation.

    Returns the translated line.
    """
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

        if word.lower().strip() == "latex":
            line = line.replace(word, r"\LaTeX{}")

    return line
