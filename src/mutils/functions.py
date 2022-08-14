from subprocess import CalledProcessError, run
from shutil import which
from typing import Any

from src.config import Config
from src.utils.logger import Logger


def build_file(log: Logger, output_folder: str, filename: str) -> None:
    """Build the LaTeX file using pdflatex."""

    if which("pdflatex") is None:
        log.logger(
            "e", "PdfLaTeX does not exists, cannot build file."
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
        log.logger("E", f"{Err}, aborting ...")


def update_conf(log: Logger, config: Config, args: Any) -> None:
    """Update the overrides of the program."""

    PARAMETERS: dict[str, Any] = {
        "filename": args.filename,
        "output_folder": args.outputfolder,
        "author": args.author,
        "date": args.date,
        "doc_font": args.font,
        "font_size": args.fontsize,
        "paper_size": args.papersize,
        "margin": args.margin,
        "indent_size": args.indent,
        "doc_font": args.font
    }

    key_: str; param: Any
    for key_, param in PARAMETERS.items(): # for overrides
        if param is not None:
            log.logger(
                "I", f"{config.__getattribute__(key_)} -> {param}"
            )
            config.__setattr__(key_, param)
