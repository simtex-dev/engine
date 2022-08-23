from shutil import copy

from src.utils.logger import Logger


def finalize(
        log: Logger, files: list[str], output_folder: str, ORIGIN: str
    ) -> None:

    if ORIGIN.startswith("./"):
        OPATH = "/".join(ORIGIN.split("/")[:-1])
    else:
        OPATH = "./"+"/".join(ORIGIN.split("/")[:-1])

    file: str
    for file in files:
        log.logger("I", f"Copying {file} into {output_folder} ...")
        filename: str = file.split("/")[-1]
        try:
            copy(
                f"{OPATH}/{file.replace('./', '')}",
                f"{output_folder}/{filename}"
            )
        except (FileNotFoundError, OSError, IOError) as Err:
            log.logger(
                "e", f"Encountered: {Err} while moving {file}, skipping ..."
            )
