from re import sub
from typing import Callable, TextIO

from src.config import Rules, Replacements
from src.utils.tex.environments.mathsec import mathsec
from src.utils.tex.environments.figure import figure
from src.utils.tex.environments.quotes import quotation
from src.utils.tex.environments.listings import listings
from src.utils.tex.text.format import format
from src.utils.logger import Logger


def body(
        log: Logger,
        rules: Rules,
        replacements: Replacements,
        in_file: str,
        out_file: TextIO
    ) -> list[str]:
    """Generate a LaTeX version of the given markdown file.

    Args:
        log -- for logging.
        rules -- rules that needs to be followed in translation.
        replacements -- math symbols that will be replaced with latex commands.
        in_file -- path of the file to be converted to LaTeX.
        out_file -- where the translated line will be written.

    Returns:
        A list of files found in the input file.
    """

    log.logger("I", "Writing the body to the document ...")

    files: list[str] = []
    ignore: int = -1

    line: str
    striptitle: Callable[
            [str, str], str
        ] = lambda line, symbol: (
            line
                .replace(symbol, "")
                .replace("\n", "")
                .strip()
        )
    section: Callable[
            [str, str, str], str
        ] = lambda symbol, line, command: (
            f"\n\\{command}"
            f"{'*' if symbol.endswith('*') else ''}"
            f"{{{striptitle(line, symbol)}}}\n"
        )

    ref_file: TextIO
    with open(in_file, "r", encoding="utf-8") as ref_file:
        ref_tex: list[str] = ref_file.readlines()

    cur: int # current index
    for cur, line in enumerate(ref_tex):
        if line in ["", "\n"] or cur <= ignore:
            continue

        # replace numerous \n, if there is any, with one \n
        line = sub(r"\n{2, 10}", "\n", line).strip()

        match (symbol := line.split()[0].strip()):
            case rules.section | rules.sectionn:
                line = section(symbol, line, "section")
            case rules.subsection | rules.subsectionn:
                line = section(symbol, line, "subsection")
            case rules.subsubsection | rules.subsubsectionn:
                line = section(symbol, line, "subsubsection")
            case rules.paragraph | rules.paragraphn:
                line = section(symbol, line, "paragraph")
            case rules.subparagraph | rules.subparagraphn:
                line = section(symbol, line, "subparagraph")
            case _:
                if line.startswith(rules.paragraph_math): # math mode
                    ignore = mathsec(
                            rules.paragraph_math,
                            line,
                            ref_tex,
                            cur,
                            out_file
                        )
                    continue
                elif line.startswith(rules.bquote):
                    ignore = quotation(
                            rules,
                            replacements,
                            ref_tex,
                            cur,
                            out_file
                        )
                    continue
                elif line.startswith(rules.code): # for code blocks
                    ignore = listings(
                            rules.code,
                            line,
                            cur,
                            ref_tex,
                            out_file
                        )
                    continue
                else:
                    skip_line: bool = figure(
                            rules.image,
                            line,
                            files,
                            out_file
                        )
                    if not skip_line:
                        line = f"\n{line}\n"
                    else:
                        continue

        out_file.write(format(rules, replacements, line, line.split()))

    return files
