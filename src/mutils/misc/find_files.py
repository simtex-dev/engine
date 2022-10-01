from os import walk
from os.path import join


def find_files(PATH: str, filetypes: str | list[str]) -> list[str]:
    """Find files to convert in the given path.

    Args:
        PATH -- where to look from.
        filetypes -- the filetypes that will be converted.

    Returns:
        The list of all files found.
    """

    files: list[str] = []

    root: str; dir: str | list[str]
    for root, _, dir in walk(PATH):
        for file in dir:
            if file.endswith(tuple(filetypes)):
                files.append(join(root, file))

    return files
