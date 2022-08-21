from re import findall

from src.config import Rules


def appearance(line: str, words: list[str], rules: Rules) -> str:
    """Formats the text in a line.

    Arguments:
        line -- line that needs to be translated.
        words -- list of words in the line split by spaces.
        rules: Rules -- rules that needs to be followed in translation.

    Returns:
        The formatted line.
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
        elif (strike := findall(rules.strike[1], line)):
            line = line.replace(
                    f"{rules.strike[0]}{strike[0]}{rules.strike[0]}",
                    f"\\sout{{{strike[0]}}}"
                )

        if word.lower().strip() == "latex":
            line = line.replace(word, r"\LaTeX{}")

    return line
