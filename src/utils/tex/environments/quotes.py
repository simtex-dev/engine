from typing import TextIO


def quotation(
        rule: str,
        sources: list[str],
        start: int,
        out_file: TextIO
    ) -> int:
    """For typesetting of block quotes using csquotes package.

    Args:
        rule -- rule that needs to be followed in translation.
        sources -- where the other lines of equation would be found.
        start -- where the parser/translator would start.
        out_file -- where the translated line will be written.

    Returns:
        An integer that marks the lines that should be skipped.
    """

    out_file.write("\n\\begin{displayquote}\n")

    end: int; quote: str
    for end, quote in enumerate(sources[start:]):
        if not quote.startswith(rule):
            out_file.write("\\end{displayquote}\n")
            break
        else:
            out_file.write(
                f"\t{quote.replace(rule, '').strip()}\n"
            )

    return end+start

