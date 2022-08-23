from os import mkdir
from os.path import exists
from typing import NoReturn

from src.utils.logger import Logger


def prep(
        log: Logger, output_folder: str, filename: str
    ) -> NoReturn | str:
    """For preparation of program before the conversion, this includes,
    checking the existence of output folder, as well as if there will be
    existing files that maybe overwritten.

    Args:
        log -- for logging.
        output_folder -- where the file will be written.
        filename -- name of the file that will be written.

    Returns:
        The path of the file, or raises systemexit.
    """


    if not exists(output_folder):
        log.logger("I", f"Creating dir: {output_folder} ...")
        mkdir(output_folder)

    file_path: str = f"{output_folder}/{filename}"
    if exists(file_path):
        match input(
                (
                    f"\033[1mINPT\033[0m\t File: {file_path}"
                    " already exists, overwrite (o)? [y/n/o] "
                )
            ).lower():
            case "y":
                log.logger(
                    "I", f"Overwriting: {file_path} with the new file ..."
                )
            case "o":
                new_filename: str = input(
                        "\033[1mINPT\033[0m\t Input another file name: "
                    )
                if not new_filename.endswith(".tex"):
                    new_filename = f"{new_filename}.tex"
                file_path = f"{output_folder}/{new_filename}"
            case _:
                log.logger(
                    "e", f"File: {file_path} already exists, aborting ..."
                )
                raise SystemExit

    return file_path
