from re import findall
from typing import TextIO

from src.config import Rules
from src.utils.tex.text.appearance import appearance


def commons(
        line: str,
        words: list[str],
        rules: Rules,
        files: list[str],
        out_file: TextIO
    ) -> None:
    """Common markdown things that needed to be translated to LaTeX.

    Arguments:
    line: str -- line that will be analyzed and translated.
    words: list[str] -- the number of words in the input line.
    rules: Rules -- rules that needs to be followed in translation.
    files: list[str] -- where the files referenced in the line will
        be appended to.
    out_file: TextIO -- where the translated line will be written.
    """

    try:
        skip_line: bool = False

        img: list[tuple[str, str]]
        link: list[tuple[str, str]]

        if (img := findall(rules.image, line)):
            out_file.write(
                "\\begin{figure}[h]\n"
                "\t\\includegraphics[width=\\textwidth]"
                f"{{{img[0][1]}}}\n"
                f"\t\\caption{{{img[0][0]}}}\n"
                "\\end{figure}\n"
            )
            skip_line = True
            files.append(img[0][1])

        for _ in range(len(words)):
            if (link := findall(rules.links, line)):
                line = line.replace(
                        f"[{link[0][0]}]({link[0][1]})",
                        f"\\href{{{link[0][0]}}}{{{link[0][1]}}}"
                    )
            elif (icodes := findall(rules.inline_code, line)):
                line = line.replace(
                        f"`{icodes[0]}`",
                        f"\\texttt{{{icodes[0]}}}"
                    )
    finally:
        if not skip_line:
            line = (
                    appearance(line, words, rules)
                        .replace("_", r"\_")
                        .replace("\n", "\n")
                )
            out_file.write(f"\n{line}\n")
