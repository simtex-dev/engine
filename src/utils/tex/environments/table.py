from typing import TextIO

from src.config import Rules, Replacements
from src.utils.tex.text.format import format
from src.utils.tex.parser.table_parse import table_parse

def table(
        rules: Rules,
        replacements: Replacements,
        start: int,
        source: list[str],
        out_file: TextIO
    ) -> int:
    """Write the parsed table to the body of the LaTeX file.

    Args:
        rules: Rules -- rules that needs to be followed in translation.
        replacements -- math symbols that will be replaced with latex commands.
        start -- where the parser/translator would start.
        source -- where the other rows would be found.
        out_file -- where the translated line will be written.

    Returns:
        An integer that denotes what line to skip.
    """

    out_file.write("\n\\begin{center}\n")

    cur: int; row: str
    for cur, row in enumerate(source[start:]):
        if "|" not in row:
            end: int = cur+start

        formatted_row: str = format(
                rules, replacements, row, row.split("|")
            )
        parsed: str | tuple[int, list[str]] = table_parse(cur, formatted_row)

        if isinstance(parsed, tuple):
            cols: str = " | ".join(["c" for _ in parsed[1]])
            out_file.write(f"\t\\begin{{tabular}}{{{cols}}}\n")
        elif isinstance(parsed, str):
            out_file.write(f"\t\t{parsed}\n")

    out_file.write("\t\\end{tabular}\n\\end{center}\n")
    return end
