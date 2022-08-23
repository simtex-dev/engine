from re import findall
from typing import TextIO


def figure(
        rule: str, line: str, files: list[str], out_file: TextIO
    ) -> bool:
    """Common markdown things that needed to be translated to LaTeX.

    Args:
        rule -- rule that needs to be followed in translation.
        line -- line that will be analyzed and translated.
        files -- where the files referenced in the line will be appended to.
        out_file -- where the translated line will be written.
    """

    skip_line: bool = False

    img: list[tuple[str, str]]
    if (img := findall(rule, line)):
        out_file.write(
            "\n\\begin{figure}[h]\n"
            "\t\\includegraphics[width=\\textwidth]"
            f"{{{img[0][1]}}}\n"
            f"\t\\caption{{{img[0][0]}}}\n"
            "\\end{figure}\n"
        )
        skip_line = True
        files.append(img[0][1])

    return skip_line
