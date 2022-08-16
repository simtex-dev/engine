from os import system
from shutil import which, copy
from typing import Any

from requests import get

from src.config import Config
from src.utils.logger import Logger
from src.misc.stdout import Signs


def build_file(log: Logger, output_folder: str, filename: str) -> None:
    """Build the LaTeX file using pdflatex."""

    if which("pdflatex") is None:
        log.logger(
            "e", "PdfLaTeX does not exists, cannot build file."
        )
        raise SystemExit

    try:
        print(
            f"{Signs.INFO} Building latex file with pdflatex."
        )
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
            log.logger("P", "Successfully built the file.")
    except OSError as Err:
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


def fix_missing_config(
        log: Logger,
        CONF_PATH: str,
        conf: bool = False,
        code_conf: bool = False
    ) -> None:
    """Fetch the backup copy of the config file or download the file."""

    if conf:
        link: str = (
                "https://raw.githubusercontent.com/iaacornus"
                "/simtex/devel/examples/config/simtex.json"
            )
        filename: str = "simtex.json"
    elif code_conf:
        link = (
            "https://raw.githubusercontent.com/iaacornus"
            "/simtex/devel/examples/config/code_conf.txt"
            )
        filename = "code_conf.txt"

    log.logger(
        "I", f"{filename} not found, using the default."
    )

    for _ in range(3):
        try:
            copy(
                f"{CONF_PATH}/{filename}.bak",
                f"{CONF_PATH}/{filename}"
            )
        except FileNotFoundError:
            try:
                log.logger(
                    "e", "Backup file not found, fetching original config ..."
                )
                with get(link, stream=True) as d_file:
                    with open(
                            f"{CONF_PATH}/{filename}.bak", "wb"
                        ) as conf_file:
                        for chunk in d_file.iter_content(chunk_size=1024):
                            if chunk:
                                conf_file.write(chunk)
            except ConnectionError as Err:
                log.logger(
                    "E", f"{Err}, cannot download {filename}, aborting ..."
                )
            else:
                continue
        else:
            log.logger("I", "Sucessfully fetched the config file.")
            return

    raise SystemExit
