from os.path import isdir
from subprocess import Popen
from typing import Any, NoReturn

from src.configs.config import Config
from src.configs.rules import Rules
from src.configs.replacements import Replacements
from src.mutils.build_tex import build_file
from src.utils.convert_file import convert_file
from src.mutils.find_files import find_files
from src.utils.logger import Logger


def convert(
        log: Logger,
        args: Any,
        rules: Rules,
        config: Config,
        replacement: Replacements,
    ) -> list[str] | NoReturn:
    """Call the converter to convert the files.

    Args:
        log -- for logging.
        args -- overrides received from arguments.
        rules -- rules that needs to be followed in translation.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        replacements -- math symbols that will be replaced with latex commands.
        input_file -- the directory of the input file.

    Returns:
        The path(s) of the converted file.
    """

    file_path: list[str] = []

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
            file_path.append(
                convert_file(
                    log,
                    args,
                    rules,
                    config,
                    replacement,
                    file
                )
            )
    else:
        file_path.append(
            convert_file(
                log,
                args,
                rules,
                config,
                replacement,
                args.input
            )
        )

    if args.build:
        for file in file_path:
            build_file(
                log,
                config.compiler,
                config.output_folder,
                file,
                args.verbose
            )
            if args.buildnview:
                try:
                    Popen(["xgd-open", file])
                except FileNotFoundError:
                    log.logger(
                        "e", "No PDF viewer found, cannot view PDF file."
                    )
    else:
        print(
            "\033[34mINFO \033[0m\t To compile the output, you "
            "use can overleaf: \033[36mhttps://www.overleaf.com/"
            "\033[0m (not sponsored) to compile the output."
        )

    return file_path
