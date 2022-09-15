from re import sub
from typing import Callable, TextIO

from src.configs.rules import Rules
from src.configs.replacements import Replacements
from src.mutils.check_if_table import check_if_table
from src.utils.tex.environments.table import table
from src.utils.tex.environments.mathsec import mathsec
from src.utils.tex.environments.figure import figure
from src.utils.tex.environments.quotes import quotation
from src.utils.tex.environments.listings import listings
from src.utils.tex.text.fix_spell import fix_spell
from src.utils.tex.text.format import format
from src.utils.logger import Logger


def body(
        log: Logger,
        rules: Rules,
        replacements: Replacements,
        autocorrect: bool,
        autocorrect_lang: str,
        replace_math_symb: bool,
        in_file: str,
        out_file: TextIO
    ) -> list[str]:
    """Generate a LaTeX version of the given markdown file.

    Args:
        log -- for logging.
        rules -- rules that needs to be followed in translation.
        replacements -- math symbols that will be replaced with latex commands.
        autocorrect -- whether to toggle autocorrect.
        autocorrect_lang -- language of autocorrect to use.
        replace_math_symb -- whether to replace the math symbols.
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

    ref_tex.append("\n")

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
                            replace_math_symb,
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
                        try:
                            if check_if_table(ref_tex[cur], ref_tex[cur+1]):
                                ignore = table(
                                        rules,
                                        replacements,
                                        cur,
                                        replace_math_symb,
                                        ref_tex,
                                        out_file
                                    )
                                continue
                            else:
                                if autocorrect:
                                    line = fix_spell(line, autocorrect_lang)
                                else:
                                    line = f"\n{line}\n"
                        except IndexError:
                            pass

        out_file.write(
            format(
                rules,
                replacements,
                line,
                line.split(),
                replace_math_symb
            )
        )

    return files
