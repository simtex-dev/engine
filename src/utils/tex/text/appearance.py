from re import findall

from src.config import Rules


def appearance(line: str, linelen: int, rules: Rules) -> str:
    for _ in range(linelen):
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
    return line
