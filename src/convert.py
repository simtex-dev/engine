from typing import TextIO

from src.config import Config, Rules
from src.utils.tex.parser.headings import headings
from src.utils.tex.parser.body import body
from src.mutils.format_body import format_body
from src.mutils.preparation import prep
from src.mutils.finalize import finalize
from src.utils.logger import Logger


def convert(
        log: Logger,
        rules: Rules,
        config: Config,
        title: str,
        in_file: str,
        filenametitle: bool
    ) -> None:
    """This unifies all the modules.

    Args:
        log -- for logging.
        rules -- rules that needs to be followed in translation.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        title -- title of the document.
        in_file -- path of the file to be converted to LaTeX.
    """

    log.logger("I", f"Converting {in_file} ...")

    OFILE_PATH: str = prep(
            log, config.output_folder, config.filename
        )

    if filenametitle and title is None:
        title = in_file.split("/")[-1].split(".")[0]
    elif title is None:
        if input(
                (
                    "\033[1mINPT\033[0m\t Title is none"
                    ", use filename as title? [y/n]"
                )
            ).lower() == "y":
            title = in_file.split("/")[-1].split(".")[0]
        else:
            title = input("\033[1mINPT\033[0m\t Input title for use: ")
            log.logger(
                "I", f"Title is none, using filename: {title} as title ..."
            )

    out_file: TextIO
    with open(OFILE_PATH, "w", encoding="utf-8") as out_file:
        start: int = headings(log, config, title, out_file)
        files: list[str] = body(log, rules, in_file, out_file)

    format_body(log, config, start, OFILE_PATH)
    finalize(log, files, config.output_folder, in_file)
