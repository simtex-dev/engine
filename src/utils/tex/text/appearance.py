from re import findall

from src.config import Rules


def appearance(line: str, parts: list[str], rules: Rules) -> str:
    part: str
    for part in parts:
        if (bold := findall(rules.bold, part)):
            line = line.replace(part, f"\\textbf{{{bold[0]}}}")
        elif (italics := findall(rules.italics, part)):
            line = line.replace(part, f"\\textit{{{italics[0]}}}")
        elif (emph := findall(rules.emph, part)):
            line = line.replace(part, f"\\emph{{{emph[0]}}}")

    return line
