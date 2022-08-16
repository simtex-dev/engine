from os import mkdir
from os.path import exists
from typing import TextIO

from config import Config, Rules
from utils.tex.sections.headings import headings
from utils.tex.sections.body import body, format_body
from utils.logger import Logger
from misc.stdout import Signs


def convert(
        log: Logger,
        rules: Rules,
        config: Config,
        title: str,
        in_file: str,
    ) -> None:
    """Main program."""

    if not exists(config.output_folder):
        mkdir(config.output_folder)

    OFILE_PATH: str
    if exists((OFILE_PATH := f"{config.output_folder}/{config.filename}")):
        if input(
                f"{Signs.INPT} File: {OFILE_PATH} already exists, overwrite? "
            ).lower() != "y":
            log.logger("e", f"File: {OFILE_PATH} already exists.")
            raise SystemExit

    out_file: TextIO
    with open(OFILE_PATH, "w", encoding="utf-8") as out_file:
        start: int = headings(log, config, title, out_file)
        body(log, rules, in_file, out_file)

    format_body(log, config, start, OFILE_PATH)
