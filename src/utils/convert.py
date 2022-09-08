from typing import Any, TextIO, NoReturn

from src.configs.config import Config
from src.configs.rules import Rules
from src.configs.replacements import Replacements
from src.utils.tex.parser.headings import headings
from src.utils.tex.parser.body import body
from src.mutils.format_body import format_body
from src.mutils.fix_file_path import fix_file_path
from src.mutils.fix_title import fix_title
from src.mutils.finalize import finalize
from src.utils.logger import Logger


def convert(
        log: Logger,
        args: Any,
        rules: Rules,
        config: Config,
        replacement: Replacements,
    ) -> str | NoReturn:
    """This unifies all the modules.

    Args:
        log -- for logging.
        args -- overrides received from arguments.
        rules -- rules that needs to be followed in translation.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        replacements -- math symbols that will be replaced with latex commands.

    Returns:
        The filepath of the output file.
    """

    log.logger("I", f"Converting {args.input} ...")

    title = fix_title(
            log,
            args.title,
            args.input,
            args.filenametitle,
            args.assumeyes
        ).replace(
            "_", r"\_"
        )
    OFILE_PATH: str = fix_file_path(
            log,
            args.input,
            config.output_folder,
            args.filename,
            args.assumeyes
        )

    try:
        out_file: TextIO
        with open(OFILE_PATH, "w", encoding="utf-8") as out_file:
            start: int = headings(log, config, title, out_file)
            files: list[str] = body(
                    log, rules, replacement, args.input, out_file
                )

        format_body(log, config, start, OFILE_PATH)
        finalize(log, files, config.output_folder, args.input)
    except (IOError, PermissionError) as Err:
        log.logger(
            "E", f"{Err}. Cannot convert the file to LaTeX, aborting ..."
        )
        raise SystemExit

    return OFILE_PATH
