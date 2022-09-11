from os.path import isdir
from typing import Any, NoReturn

from src.configs.config import Config
from src.configs.rules import Rules
from src.configs.replacements import Replacements
from src.utils.convert_file import convert_file
from src.mutils.find_files import find_files
from src.utils.logger import Logger


def convert(
        log: Logger,
        args: Any,
        rules: Rules,
        config: Config,
        replacement: Replacements,
        autocorrect: bool = False
    ) -> str | NoReturn:
    """Call the converter to convert the files.

    Args:
        log -- for logging.
        args -- overrides received from arguments.
        rules -- rules that needs to be followed in translation.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        replacements -- math symbols that will be replaced with latex commands.
        input_file -- the directory of the input file.
        autocorrect -- whether to toggle autocorrect.

    Returns:
        The filepath of the output file.
    """


    if isdir(args.input):
        log.logger(
            "I",
            (
                f"The input: {args.input} is a "
                "directory, converting all files ending"
                f" with: {rules.files} to LaTeX ..."
            )
        )
        files: list[str] = find_files(args.input, rules.files)

        cur: int; file: str
        for cur, file in enumerate(files):
            log.logger(
                "I", f"Converting the {cur} in directory: {args.input}"
            )
            convert_file(
                log,
                args,
                rules,
                config,
                replacement,
                file,
                autocorrect
            )
    else:
        convert_file(
            log,
            args,
            rules,
            config,
            replacement,
            args.input,
            autocorrect
        )

