from re import findall
from typing import TextIO

from src.config import Rules
from src.utils.tex.text.appearance import appearance


def commons(
        line: str,
        linelen: int,
        rules: Rules,
        files: list[str],
        out_file: TextIO
    ) -> None:
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

        for _ in range(linelen):
            print(line)
            if (link := findall(rules.links, line)):
                line = line.replace(
                        f"[{link[0][0]}]({link[0][1]})",
                        f"\\href{{{link[0][0]}}}{{{link[0][1]}}}"
                    )
            elif (icodes := findall(rules.inline_code, line)):
                print(icodes)
                line = line.replace(
                        f"`{icodes[0]}`",
                        f"\\texttt{{{icodes[0]}}}"
                    )
    finally:
        if not skip_line:
            line = (
                    appearance(line, linelen, rules)
                        .replace("_", r"\_")
                        .replace("\n", "\n")
                )
            out_file.write(f"\n{line}\n")
