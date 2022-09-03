from shutil import copy

from src.utils.logger import Logger


def finalize(
        log: Logger, files: list[str], output_folder: str, origin: str
    ) -> None:
    """Finishes the job of conversion, which includes copying the
    referenced file into the outfule folder among others.

    Args:
        log -- for logging.
        files -- list of paths of referenced files.
        output_folder -- where the file will be written.
        origin -- the path of the input file.

    Returns:
        The path of the file, or raises systemexit.
    """

    if origin.startswith("./"):
        OPATH = "/".join(origin.split("/")[:-1])
    else:
        OPATH = "./"+"/".join(origin.split("/")[:-1])

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
