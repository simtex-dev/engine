from typing import TextIO

from src.config import Rules, Replacements
from src.utils.tex.text.format import format


def quotation(
        rules: Rules,
        replacements: Replacements,
        sources: list[str],
        start: int,
        out_file: TextIO
    ) -> int:
    """For typesetting of block quotes using csquotes package.

    Args:
        rule -- rule that needs to be followed in translation.
        replacements -- math symbols that will be replaced with latex commands.
        sources -- where the other lines of equation would be found.
        start -- where the parser/translator would start.
        out_file -- where the translated line will be written.

    Returns:
        An integer that marks the lines that should be skipped.
    """

    out_file.write("\n\\begin{displayquote}\n")

    end: int; quote: str
    for end, quote in enumerate(sources[start:]):
        if not quote.startswith(rules.bquote):
            out_file.write("\\end{displayquote}\n")
            break
        else:
            line: str = format(
                    rules,
                    replacements,
                    quote.replace(rules.bquote, '').strip(),
                    quote.split()
                )
            out_file.write(f"\t{line}\n")

    return end+start

