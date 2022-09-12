from collections import Counter
from typing import TextIO

from src.configs.rules import Rules
from src.configs.replacements import Replacements
from src.utils.tex.text.format import format
from src.utils.tex.parser.table_parse import table_parse


def table(
        rules: Rules,
        replacements: Replacements,
        start: int,
        replace_math_symb: bool,
        source: list[str],
        out_file: TextIO
    ) -> int:
    """Write the parsed table to the body of the LaTeX file.

    Args:
        rules: Rules -- rules that needs to be followed in translation.
        replacements -- math symbols that will be replaced with latex commands.
        start -- where the parser/translator would start.
        replace_math_symb -- whether to replace the math symbols.
        source -- where the other rows would be found.
        out_file -- where the translated line will be written.

    Returns:
        An integer that denotes what line to skip.
    """

    out_file.write("\n\\begin{center}\n")

    cur: int; row: str
    for cur, row in enumerate(source[start:]):
        row = row.replace("\n", "").strip()

        if row.strip() in ["\n", ""]:
            end: int = cur+start
            break

        parsed: str | tuple[
                int, list[str], str
            ] = table_parse(
                cur,
                format(
                    rules,
                    replacements,
                    row,
                    row.split("|"),
                    replace_math_symb
                )
            )

        if isinstance(parsed, tuple):
            cols: str = " | ".join(["c" for _ in parsed[1]])
            line: str = (
                    f"\t\\begin{{tabular}}{{| {cols} |}}"
                    f"\t\t\\hline\n\t\t{parsed[2]} \\\\"
                )
        elif isinstance(parsed, str):
            if parsed == r"\hline":
                line = f"\n\t\t{parsed}"
            else:
                line = f"\n\t\t{parsed} \\\\"

        out_file.write(line)

    out_file.write(
        (
            "\t\t\\hline\n\t"
            "\\end{tabular}\n"
            "\\end{center}\n"
        )
    )
    return end
