from os import walk
from os.path import join
from typing import TextIO


def find_module(PATH: str = "src") -> list[str]:
    """Find modules in the given path.

    Args:
        PATH -- where to look from.

    Returns:
        The list of all modules found.
    """

    modules: list[str] = []

    root: str; dir: str | list[str]
    for root, _, dir in walk(PATH):
        for file in dir:
            if file.endswith(".py") and not file.endswith("__init__.py"):
                modules.append(join(root, file).removesuffix(".py"))

    return modules


def get_dependencies(source: str) -> list[str]:
    """Get the listed dependencies in requirements.txt

    Args:
        source -- requirements.txt

    Returns:
        The list of dependencies.
    """

    try:
        dep_list: TextIO
        with open(source, "r", encoding="utf-8") as dep_list:
            deps: list[str] = dep_list.readlines()
    except FileNotFoundError as Err:
        raise SystemExit("Cannot fetch dependencies.")

    return [
        dep.replace("\n", "") for dep in deps if dep not in ["", "\n"]
    ]

