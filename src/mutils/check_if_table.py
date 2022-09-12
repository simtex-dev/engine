from collections import Counter


def check_if_table(cur_line: str, sec_line: str) -> bool:
    """Check if the line is a beginning of a table.

    This works by evaluating if the current line and the second
    line contains a marker of a table, which is | and ---.

    Args:
        cur_line -- the current line.
        sec_line -- the line after the current line.

    Returns:
        Whether the line is a beginning of table or not.
    """

    if Counter(cur_line)["|"] > 1 and Counter(sec_line)["-"] > 3:
        return True

    return False
