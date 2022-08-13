from os import mkdir
from pathlib import Path
from os.path import exists
from shutil import copy
from json import load
from typing import IO, Any, NoReturn

from src.utils.config import Config, Rules
from src.utils.logger import Logger


class ConfParse:
    """Parse the JSON configuration file."""

    def __init__(self, log: Logger) -> None:
        """Check the config file in instantiation before proceeding."""

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
                        "E", f"Encountered: {Err}. Cannot create: {paths}"
                    )

        if not exists(f"{self.CONF_PATH}/simtex.json"):
            self.log.logger(
                "E", f"Config file not found, used the default."
            )
            try:
                copy(
                    f"{self.CONF_PATH}/simtex.json.bak",
                    f"{self.CONF_PATH}/simtex.json"
                )
            except FileNotFoundError:
                self.log.logger("E", "Backup file does not exists.")

    def fetch(self) -> list[dict[str, Any]] | NoReturn:
        """Parse and replace the overriden parameters in the CLI."""

        try:
            conf_file: IO[Any]
            with open(
                    f"{self.CONF_PATH}/simtex.json",
                    "r",
                    encoding="utf-8"
                ) as conf_file:
                raw_conf: list[dict[str, Any]] = load(conf_file)

        except (FileNotFoundError, PermissionError) as Err:
            self.log.logger("E", f"Encountered {Err}, aborting ...")
            raise SystemExit
        else:
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
            raw_conf["INLINE_CODE"]
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
            raw_conf["CODE_CONF"],
            raw_conf["PACKAGES"],
            raw_conf["FOOTNOTE"],
            raw_conf["SECTION_SIZES"],
            raw_conf["LINKS"],
            raw_conf["LINK_COLOR"],
            raw_conf["AUTHOR"],
            raw_conf["DATE"],
            raw_conf["MAKE_TITLE"],
            raw_conf["FILE_NAME"],
            raw_conf["OUTPUT_FOLDER"]
        )
