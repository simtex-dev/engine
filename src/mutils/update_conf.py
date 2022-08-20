from typing import Any

from src.config import Config
from src.utils.logger import Logger


def update_conf(log: Logger, config: Config, args: Any) -> None:
    """Update the overrides of the program.

    Arguments:
    log: Logger -- for logging.
    config: Config -- configuration of the document metadata, which includes,
        formatting, packages to use among others, refer to simtex.json.
    args: Any -- overrides received from arguments.
    """

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
        "doc_font": args.font,
        "compiler": args.compiler
    }

    key_: str; param: Any
    for key_, param in PARAMETERS.items(): # for overrides
        if param is not None:
            log.logger(
                "I",
                f"Override: {key_} {config.__getattribute__(key_)} -> {param}"
            )
            config.__setattr__(key_, param)
