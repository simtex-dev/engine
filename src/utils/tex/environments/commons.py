from re import findall
from typing import TextIO

from src.config import Rules
from src.utils.tex.text.appearance import appearance


def commons(
        line: str,
        parts: list[str],
        rules: Rules,
        files: list[str],
        out_file: TextIO
    ) -> None:
    try:
        new_line: str = line
        skip_line: bool = False

        part: str
        for part in parts:
            img_results: list[tuple[str, str]]
            link_results: list[tuple[str, str]]

            if (img_results := findall(rules.image, part)):
                out_file.write(
                    "\\begin{figure}[h]\n"
                    "\t\\includegraphics[width=\\textwidth]"
                    f"{{{img_results[0][1]}}}\n"
                    f"\t\\caption{{{img_results[0][0]}}}\n"
                    "\\end{figure}\n"
                )
                skip_line = True
                files.append(img_results[0][1])
                break

            if (link_results := findall(rules.links, part)):
                link: tuple[str, str]
                for link in link_results:
                    new_line = new_line.replace(
                            f"[{link[0]}]({link[1]})",
                            f"\\href{{{link[0]}}}{{{link[1]}}}"
                        )
            elif (
                    inline_codes := findall(
                            rules.inline_code, part
                        )
                ):
                codes: tuple[str]
                for codes in inline_codes:
                    new_line = new_line.replace(
                            f"`{codes}`",
                            f"\\texttt{{{codes}}}"
                        )
    finally:
        if not skip_line:
            new_line = (
                    appearance(line, len(parts), rules)
                        .replace("_", r"\_")
                        .replace("\n", "\n")
                )
            out_file.write(f"\n{new_line}\n")
