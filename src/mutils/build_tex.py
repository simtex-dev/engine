from shutil import which
from subprocess import (
    run,
    CalledProcessError,
    DEVNULL
)

from src.utils.logger import Logger


def build_file(
        log: Logger,
        compiler: str,
        output_folder: str,
        filename: str,
        verbose: bool
    ) -> None:
    """Build the LaTeX file using pdflatex, if exists.

    Args:
        log -- for logging.
        output_folder -- where the built pdf and its file will be
            placed.
        filename -- name of the LaTeX file.
    """

    if which("pdflatex") is None:
        log.logger(
            "e", "PdfLaTeX does not exists, cannot build file."
        )
        raise SystemExit

    try:
        log.logger("I", f"Building {filename} with pdflatex ...")
        cmd: list[str] = [
                compiler,
                "-synctex=1",
                "-interaction=nonstopmode",
                f"-output-directory={output_folder}",
                filename
            ]

        if verbose:
            rcode = run(cmd).returncode
        else:
            rcode = run(cmd, stdout=DEVNULL).returncode

        if rcode != 0:
            raise CalledProcessError(rcode, cmd)
        else:
            log.logger("I", "Successfully built the file.")
    except (OSError, CalledProcessError) as Err:
        log.logger("E", f"{Err}. Cannot build LaTeX file.")



