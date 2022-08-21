from shutil import which
from subprocess import (
    run,
    CalledProcessError,
    CompletedProcess,
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
        log.logger("P", f"Building {filename} with pdflatex ...")
        cmd: list[str] = [
                compiler,
                "-synctex=1",
                "-interaction=nonstopmode",
                f"-output-directory={output_folder}",
                f"{filename}"
            ]

        if verbose:
            rcode: CompletedProcess = run(cmd)
        else:
            rcode: CompletedProcess = run(cmd, stdout=DEVNULL)

        if rcode.returncode != 0:
            raise CalledProcessError(rcode.returncode, cmd)
        else:
            log.logger("I", "Successfully built the file.")
    except (OSError, CalledProcessError) as Err:
        log.logger("E", f"{Err}. Cannot build LaTeX file.")



