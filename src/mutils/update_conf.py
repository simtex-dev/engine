from difflib import SequenceMatcher as SeqMatch
from typing import Any

from src.config import Config
from src.utils.logger import Logger


def update_conf(log: Logger, config: Config, args: Any) -> None:
    """Update the overrides of the program.

    Args:
        log -- for logging.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        args -- overrides received from arguments.
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
        "compiler": args.compiler,
        "encode": args.encoding
    }

    key_: str; param: Any
    for key_, param in PARAMETERS.items(): # for overrides
        if param is not None:
            if args.compiler is not None and args.compiler not in (
                    compilers := ["xetex", "pdflatex", "luatex"]
                ): # if compiler is not in options
                pos_compilers: list[float] = [
                        SeqMatch(
                            args.compiler, option
                        ).ratio() for option in compilers
                    ]
                compiler: str = compilers[
                        pos_compilers.index(max(pos_compilers))
                    ]

                if input(
                        f"\033[1mINPT\033[0m Did you mean {compiler}? "
                    ).lower() == "y":
                    args.compiler = compiler
                else:
                    args.compiler = "pdflatex"
                    log.logger(
                        "e", "Compiler option not recognized, using pdflatex"
                    )

            log.logger(
                "I",
                f"Override: {key_} {config.__getattribute__(key_)} -> {param}"
            )
            config.__setattr__(key_, param)
