from string import digits
from typing import TextIO

from src.utils.logger import Logger


def tex_enumerate(
        start: int, source: list[str], out_file: TextIO
    ) -> int:
    """For enumerate/lists environment.

    Args:
        start -- where the parser/translator would start.
        source -- where the other lines of equation would be found.
        out_file -- where the output will be written.

    Returns:
        The index of line where the enumerate ends.
    """

    out_file.write("\n\\begin{enumerate}\n")

    end: int; line: str
    for end, line in enumerate(source[start:]):
        if line.split()[1].startswith(""):
            out_file.write(
                f"\t\\item {line}\n"
            )
        else:
            out_file.write("\\end{enumerate}\n")

    return end+start+1
