from shutil import which
from os import system

from src.utils.logger import Logger


def build_file(log: Logger, output_folder: str, filename: str) -> None:
    """Build the LaTeX file using pdflatex, if exists.

    Arguments:
    log: Logger -- for logging.
    output_folder: str -- where the built pdf and its file will be placed.
    filename: str -- name of the LaTeX file.
    """

    if which("pdflatex") is None:
        log.logger(
            "e", "PdfLaTeX does not exists, cannot build file."
        )
        raise SystemExit

    try:
        log.logger("P", f"Building {filename} with pdflatex ...")
        rcode = system(
                (
                    "pdflatex "
                    "-synctex=1 "
                    "-interaction=nonstopmode "
                    f"-output-directory={output_folder} "
                    f"{filename}"
                ),
            )
        if rcode == 0:
            log.logger("I", "Successfully built the file.")
    except OSError as Err:
        log.logger("E", f"{Err}. Cannot build LaTeX file.")



