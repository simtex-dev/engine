from os import mkdir
from os.path import exists
from re import sub
from typing import NoReturn

from src.mutils.prompts import prompt
from src.utils.logger import Logger


def fix_file_path(
        log: Logger,
        in_file: str,
        output_folder: str,
        filename: str,
        assume_yes: bool
    ) -> str | NoReturn:
    """Update the path of the output file if there are any errors or
    exceptions that is deemed to be encountered.

    Args:
        log -- for logging.
        output_folder -- where the file will be written.
        filename -- name of the file that will be written.
        assume_yes -- whether to assume yes or not.

    Returns:
        The path of the file, or raises systemexit.
    """

    if not exists(output_folder):
        log.logger("I", f"Creating dir: {output_folder} ...")
        mkdir(output_folder)

    if not filename or filename is None:
        in_filename: str = in_file.split("/")[-1].split(".")[0].strip()
        new_filename = sub(
                r"( ?) +", r"_", in_filename
            ).removesuffix(".tex")
        file_path: str = f"{output_folder}/{new_filename}.tex"
        log.logger(
            "I",
            f"Filename is None, using input filename"
            f": {in_filename} as filename."
        )
    else:
        file_path = f"{output_folder}/{filename.removesuffix('.tex')}.tex"

    if exists(file_path):
        match prompt(
                (
                    f"File: {file_path} exists overwrite (y)"
                    ", abort (n), or rename (r)? [y/n/r] "
                ),
                assume_yes,
                other_cases=True
            ):
            case "y":
                log.logger(
                    "I",
                    f"Overwriting: {file_path} with the new file ..."
                )
            case "r":
                new_filename = input(
                        "\033[1mINPT\033[0m\t Input another file name: "
                    ).removesuffix(".tex")
                file_path = f"{output_folder}/{new_filename}.tex"
            case _:
                log.logger(
                    "E",
                    f"File: {file_path} already exists, aborting ..."
                )
                raise SystemExit

    return file_path
