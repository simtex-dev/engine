from re import findall
from turtle import title

from typing import Any, Callable, TextIO, IO

from src.config import Config, Rules
from src.utils.tex.environments.mathsec import mathsec
from src.utils.tex.environments.commons import commons
from src.utils.logger import Logger


def body(
        log: Logger, rules: Rules, in_file: str, out_file: TextIO
    ) -> list[str]:
    """Generate a LaTeX version of the given markdown file.

    Arguments:
    out_file: str -- the path of the file to convert (reference file).
    rules: object -- the rules to follow for parsing.
    out_file: textio -- where the output will be written.
    """

    line: str
    striptitle: Callable[..., str] = lambda line, def_rule: (
            line
                .replace(def_rule, "")
                .replace("\n", "")
                .strip()
        )
    title: Callable[..., str] = lambda line, command, def_rule: (
            f"\n\\{command}{{{striptitle(line, def_rule)}}}\n"
        )

    files: list[str] = []

    ref_file: TextIO
    with open(in_file, "r", encoding="utf-8") as ref_file:
        ref_tex: list[str] = ref_file.readlines()

    ref: int = -1

    log.logger("I", "Writing the body to the document ...")

    i: int
    for i, line in enumerate(ref_tex):
        if line in ["", "\n"]:
            continue

        if i <= ref:
            continue

        match line.split()[0].strip():
            case rules.section:
                out_file.write(
                    title(line, "section", rules.section)
                )
            case rules.subsection:
                out_file.write(
                    title(line, "subsection", rules.subsection)
                )
            case rules.subsubsection:
                out_file.write(
                    title(line, "subsubsection", rules.subsubsection)
                )
            case rules.paragraph:
                out_file.write(
                    title(line, "paragraph", rules.paragraph)
                )
            case rules.subparagraph:
                out_file.write(
                    title(line, "subparagraph", rules.subparagraph)
                )
            case _:
                if line.startswith(rules.paragraph_math): # math mode
                    ref = mathsec(
                        line,
                        rules.paragraph_math,
                        out_file,
                        ref_tex.copy(),
                        i,
                        ref
                    )
                elif line.startswith(rules.code): # for code blocks
                    language: str = line[3:].replace("\n", "")
                    out_file.write(
                        f"\n\\begin{{lstlisting}}"
                        f"[language={language.upper()}]\n"
                    )

                    code: str; n: int
                    for n, code in enumerate(ref_tex.copy()[i+1:]):
                        if code.strip() == rules.code:
                            out_file.write("\end{lstlisting}\n")
                            ref = n+i+1
                            break

                        out_file.write(code)
                else:
                    commons(
                        line,
                        line.split(" "),
                        rules,
                        files,
                        out_file
                    )


    return files
