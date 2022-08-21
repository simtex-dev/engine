from os import mkdir
from os.path import exists, expanduser
from pathlib import Path
from json import load
from typing import IO, Any, Optional

from src.config import Config, Rules
from src.mutils.fix_missing_conf import fix_missing_config
from src.utils.logger import Logger


class ConfParse:
    """Parse the JSON configuration file."""

    def __init__(self, log: Logger, test: Optional[bool] = False) -> None:
        """Check the config file in instantiation before proceeding.

        Args:
            log -- for logging.
            test -- to know if the execution is for unit testing.
        """

        self.log: Logger = log
        self.HOME: Path = Path.home()
        self.BASE_CONF_PATH: str = f"{self.HOME}/.config"
        self.CONF_PATH: str = f"{self.BASE_CONF_PATH}/simtex"

        paths: str
        for paths in [self.BASE_CONF_PATH, self.CONF_PATH]:
            if not exists(paths):
                try:
                    mkdir(paths)
                except (SystemError, OSError, IOError) as Err:
                    self.log.logger(
                        "E", f"{Err}. Cannot create: {paths}, aborting ..."
                    )

        if not exists(f"{self.CONF_PATH}/simtex.json"):
            fix_missing_config(self.log, self.CONF_PATH, True)
        elif not exists(f"{self.CONF_PATH}/code_conf.txt"):
            fix_missing_config(self.log, self.CONF_PATH, code_conf=True)

        if test:
            self.CONF_PATH = "./examples/config"

    def fetch(self) -> list[dict[str, Any]]:
        """Fetch the config file."""

        try:
            conf_file: IO[Any]
            with open(
                    f"{self.CONF_PATH}/simtex.json",
                    "r",
                    encoding="utf-8"
                ) as conf_file:
                raw_conf: list[dict[str, Any]] = load(conf_file)
        except (FileNotFoundError, PermissionError) as Err:
            self.log.logger(
                "E", f"{Err}. Cannot fetch config file, aborting ..."
            )

        return raw_conf

    def rules(self) -> Rules:
        """Parse the config of the rules of converter."""

        raw_conf: dict[str, Any] = self.fetch()[0]

        return Rules(
            raw_conf["FOR"],
            raw_conf["CODE_BLOCKS"],
            raw_conf["IMAGE"],
            raw_conf["LINKS"],
            raw_conf["SECTION"],
            raw_conf["SUBSECTION"],
            raw_conf["SUBSUBSECTION"],
            raw_conf["PARAGRAPH"],
            raw_conf["SUBPARAGRAPH"],
            raw_conf["INLINE_MATH"],
            raw_conf["PARAGRAPH_MATH"],
            raw_conf["INLINE_CODE"],
            raw_conf["BOLD"],
            raw_conf["ITALICS"],
            raw_conf["EMPH"],
            raw_conf["STRIKE"],
            raw_conf["SUPSCRIPT"],
            raw_conf["SUBSCRIPT"],
            raw_conf["ULINE"],
            raw_conf["QUOTE"],
            raw_conf["BQUOTE"]
        )

    def conf(self) -> Config:
        """Parse the config of the LaTeX file."""

        raw_conf: dict[str, Any] = self.fetch()[1]

        return Config(
            raw_conf["DOC_CLASS"],
            raw_conf["DEF_FONT"],
            raw_conf["FONT_SIZE"],
            raw_conf["MARGIN"],
            raw_conf["PAPER_SIZE"],
            raw_conf["INDENT_SIZE"],
            raw_conf["SLOPPY"],
            raw_conf["CODE_FONT"],
            raw_conf["CFONT_SCALE"],
            raw_conf["CODE_CONF"].replace(
                "<HOME>", expanduser("~")
            ),
            raw_conf["PACKAGES"],
            raw_conf["FOOTNOTE"],
            raw_conf["SECTION_SIZES"],
            raw_conf["LINKS"],
            raw_conf["LINK_COLOR"],
            raw_conf["AUTHOR"],
            raw_conf["DATE"],
            raw_conf["MAKE_TITLE"],
            raw_conf["FILE_NAME"],
            raw_conf["OUTPUT_FOLDER"],
            raw_conf["COMPILER"],
            raw_conf["ENCODE"]
        )
