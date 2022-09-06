from re import sub
from collections import Counter


def table_parse(start: int, line: str) -> str | tuple[int, list[str]]:
    """Parse the list of strings evaluated to be as table.

    Args:
        start -- where the parser/translator would start.
        line -- line that will be analyzed and translated.

    Returns:
        The row of table in format compatible with LaTeX.
    """

    item: str = sub(
            " +",
            " ",
            (
                line
                    .removesuffix("|")
                    .removeprefix("|")
                    .replace("|", " & ")
            )
        )
    if start == 0:
        items: list[str] = item.split("&")
        return len(items), [item.strip() for item in items]
    elif Counter(line)["-"] > 3:
        return r"\hline"

    return item
