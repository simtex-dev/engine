from collections import Counter


def check_if_table(start: int, source: list[str]) -> bool:
    """Check if the line is a beginning of a table.

    Args:
        start -- where the parser/translator would start.
        source -- where the other lines of table may be found

    Returns:
        Whether the line is a beginning of table or not.
    """

    cur: int; table: str
    for cur, table in enumerate(source[start:]):
        # determine if the set of lines is
        # table using "-" and "|" as marker
        if Counter(table)["|"] > 1 and Counter(source[cur+1])["-"] > 1:
            return True

    return False
