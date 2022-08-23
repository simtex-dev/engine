from typing import TextIO

from src.config import Rules
from src.utils.logger import Logger


def quotation(
        log: Logger,
        line: str,
        rules: Rules,
        sources: list[str],
        start: int,
        out_file: TextIO
    ) -> int:
    """For typesetting of block quotes using csquotes package.

    Args:
        line -- line that will be analyzed and translated.
        start -- where the parser/translator would start.
        out_file -- where the translated line will be written.

    Returns:
        An integer that marks the lines that should be skipped.
    """

    end: int
    try:
        for end, quote in enumerate(sources[start:]):
            if not quote.startswith(rules.bquote):
                return end+start
            else:
                out_file.write(
                    quote.replace(rules.bquote, "")
                )
    except IOError as Err:
        log.logger("E", f"{Err}. Cannot write to file, aborting ...")
        raise SystemExit
