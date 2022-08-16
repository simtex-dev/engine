from shutil import copy
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
        _title: str,
        in_file: str,
    ) -> None:
    """Main program."""

    OPATH: str = "/".join(in_file.split("/")[:-1])

    if not exists(config.output_folder):
        mkdir(config.output_folder)

    if _title is None:
        _title = in_file.split("/")[-1]
        print(
            f"{Signs.INFO} Title is none, using the {_title} as title ..."
        )

    OFILE_PATH: str
    if exists((OFILE_PATH := f"{config.output_folder}/{config.filename}")):
        if input(
                f"{Signs.INPT} File: {OFILE_PATH} already exists, overwrite? "
            ).lower() != "y":
            log.logger("e", f"File: {OFILE_PATH} already exists.")
            raise SystemExit

    out_file: TextIO
    with open(OFILE_PATH, "w", encoding="utf-8") as out_file:
        start: int = headings(log, config, _title, out_file)
        files: list[str] = body(log, rules, in_file, out_file)

    format_body(log, config, start, OFILE_PATH)

    file: str
    for file in files:
        print(f"{Signs.INFO} Copying {file} into {config.output_folder} ...")
        filename: str = file.split("/")[-1]
        try:
            copy(
                f"{OPATH}/{file.replace('./', '')}",
                f"{config.output_folder}/{filename}"
            )
        except (FileNotFoundError, OSError, IOError) as Err:
            log.logger("e", f"Encountered: {Err} while moving {file}")
