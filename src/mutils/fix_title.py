from typing import Any

from src.utils.logger import Logger


def fix_title(
        log: Logger, title: Any, in_file: str, filenametitle: bool
    ) -> str | Any:
    """Update the title of the document.

    Args:
        log -- for logger.
        title -- title of the document from argument.
        in_file -- the path of input file.
        filenametitle -- whether to use filename as title.

    Returns:
        The new title of the document.
    """

    if filenametitle and title is None:
        title = in_file.split("/")[-1].split(".")[0]
    elif title is None:
        if input(
                (
                    "\033[1mINPT\033[0m\t Title is none"
                    ", use filename as title? [y/n] "
                )
            ).lower() == "y":
            title = in_file.split("/")[-1].split(".")[0]
        else:
            title = input("\033[1mINPT\033[0m\t Input title for use: ")
            log.logger(
                "I", f"Title is none, using filename: {title} as title ..."
            )

    return title
