from os import mkdir
from os.path import exists
from typing import NoReturn

from src.utils.logger import Logger


def prep(log: Logger, output_folder: str, filename: str) -> NoReturn | str:

    if not exists(output_folder):
        log.logger("I", f"Creating dir: {output_folder} ...")
        mkdir(output_folder)

    FILE_PATH: str
    if exists((FILE_PATH := f"{output_folder}/{filename}")):
        match input(
                (
                    f"\033[1mINPT\033[0m\t File: {FILE_PATH}"
                    " already exists, overwrite (o)? [y/n/o] "
                )
            ).lower():
            case "y":
                log.logger(
                    "I", f"Overwriting: {FILE_PATH} with the new file ..."
                )
            case "o":
                new_filename: str = input(
                        "\033[1mINPT\033[0m\t Input another file name: "
                    )
                if not new_filename.endswith(".tex"):
                    new_filename = f"{new_filename}.tex"
                FILE_PATH = f"{output_folder}/{new_filename}"
            case _:
                log.logger(
                    "e", f"File: {FILE_PATH} already exists, aborting ..."
                )
                raise SystemExit

        return FILE_PATH
