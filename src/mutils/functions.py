from shutil import which
from subprocess import run, CalledProcessError

from src.utils.logger import Logger


def build_file(log: Logger, output_folder: str, filename: str) -> None:
    """Build the LaTeX file using pdflatex."""

    if which("pdflatex") is None:
        log.logger(
            "E", "PdfLaTeX does not exists, cannot build file."
        )
        raise SystemExit

    try:
        rcode = run(
                [
                    "pdflatex",
                    "-output-directory=",
                    output_folder,
                    filename
                ],
                capture_output=True
            )
        if rcode.returncode == 0:
            log.logger("P", "Successfully built the file.")
    except CalledProcessError as Err:
        log.logger("E", f"CalledProcessError raised: {Err}, aborting ...")
