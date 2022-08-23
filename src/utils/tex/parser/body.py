from re import sub
from typing import Callable, TextIO

from src.config import Rules
from src.utils.tex.environments.mathsec import mathsec
from src.utils.tex.environments.figure import figure
from src.utils.tex.environments.quotes import quotation
from src.utils.tex.environments.listings import listings
from src.utils.tex.text.format import format
from src.utils.logger import Logger


def body(
        log: Logger, rules: Rules, in_file: str, out_file: TextIO
    ) -> list[str]:
    """Generate a LaTeX version of the given markdown file.

    Args:
        log -- for logging.
        rules -- rules that needs to be followed in translation.
        in_file -- path of the file to be converted to LaTeX.
        out_file -- where the translated line will be written.

    Returns:
        A list of files found in the input file.
    """

    line: str
    striptitle: Callable[
            [str, str], str
        ] = lambda line, def_rule: (
            line
                .replace(def_rule, "")
                .replace("\n", "")
                .strip()
        )
    title: Callable[
            [str, str, str], str
        ] = lambda line, command, def_rule: (
            f"\n\\{command}{{{striptitle(line, def_rule)}}}\n"
        )

    files: list[str] = []

    ref_file: TextIO
    with open(in_file, "r", encoding="utf-8") as ref_file:
        ref_tex: list[str] = ref_file.readlines()

    ignore: int = -1

    log.logger("I", "Writing the body to the document ...")

    cur: int # current index
    for cur, line in enumerate(ref_tex):
        if line in ["", "\n"] or cur <= ignore:
            continue

        # replace numerous \n, if there is any, with one \n
        line = sub(r"\n{2, 10}", "\n", line).strip()

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
                    ignore = mathsec(
                            rules.paragraph_math,
                            line,
                            ref_tex,
                            cur,
                            out_file
                        )
                elif line.startswith(rules.bquote):
                    ignore = quotation(
                            rules.bquote,
                            ref_tex,
                            cur,
                            out_file
                        )
                elif line.startswith(rules.code): # for code blocks
                    ignore = listings(
                            rules.code,
                            line,
                            cur,
                            ref_tex,
                            out_file
                        )
                else:
                    skip_line: bool = figure(
                            rules.image,
                            line,
                            files,
                            out_file
                        )
                    if not skip_line:
                        line = (
                                format(rules, line, line.split())
                                    .replace("_", r"\_")
                            )
                        out_file.write(f"\n{line}\n")

    return files
