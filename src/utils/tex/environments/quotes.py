from typing import TextIO

from src.configs.rules import Rules
from src.configs.replacements import Replacements
from src.utils.tex.text.format import format


def quotation(
        rules: Rules,
        replacements: Replacements,
        sources: list[str],
        start: int,
        replace_math_symb: bool,
        out_file: TextIO
    ) -> int:
    """For typesetting of block quotes using csquotes package.

    Args:
        rule -- rule that needs to be followed in translation.
        replacements -- math symbols that will be replaced with latex commands.
        sources -- where the other lines of equation would be found.
        start -- where the parser/translator would start.
        replace_math_symb -- whether to replace the math symbols.
        out_file -- where the translated line will be written.

    Returns:
        An integer that marks the lines that should be skipped.
    """

    out_file.write("\n\\begin{displayquote}\n")

    cur: int; quote: str
    for cur, quote in enumerate(sources[start:]):
        if not quote.startswith(rules.bquote):
            out_file.write("\\end{displayquote}\n")
            break
        else:
            line: str = format(
                    rules,
                    replacements,
                    quote.replace(rules.bquote, '').strip(),
                    quote.split(),
                    replace_math_symb
                )
            out_file.write(f"\t{line}\n")

    return cur+start

