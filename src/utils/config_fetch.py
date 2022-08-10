from os import mkdir
from pathlib import Path
from os.path import exists
from shutil import copy
from json import load
from typing import IO, Any, NoReturn, Optional
from datetime import datetime

from src.utils.config import Config, Rules
from src.misc.stdout import Signs
from src.utils.logger import Logger


class ConfParse:
    """Parse the JSON configuration file."""

    def __init__(
            self, log: Logger, overrides: Optional[dict[str, Any]] = None
        ) -> None:
        """Check the config file in instantiation before proceeding."""

        self.log: Logger = log
        self.HOME: Path = Path.home()
        self.BASE_CONF_PATH: str = f"{self.HOME}/.config"
        self.CONF_PATH: str = f"{self.BASE_CONF_PATH}/simtex"
        self.overrides: Optional[dict[str, Any]] = overrides

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

    def parse(self) -> list[dict[str, Any]] | NoReturn:
        """Parse and replace the overriden parameters in the CLI."""

        try:
            conf_file: IO[Any]
            with open(
                    f"{self.CONF_PATH}/simtex.json",
                    "r",
                    encoding="utf-8"
                ) as conf_file:
                raw_conf: list[dict[str, Any]] = load(conf_file)

            conf: dict[str, Any] = raw_conf[0]
            if self.overrides is not None:
                val: str
                for val in self.overrides.keys():
                    if val in list(conf.keys()):
                        print(
                            (
                                f"{Signs.INFO} {conf[val]}"
                                f"-> {self.overrides[val]}"
                            )
                        )
                        conf[val] = self.overrides[val]
        except (FileNotFoundError, PermissionError) as Err:
            self.log.logger("E", f"Encountered {Err}, aborting ...")
            raise SystemExit
        else:
            return raw_conf

    def rules(self) -> Rules:
        """Parse the config of the rules of converter."""

        raw_conf: dict[str, Any] = self.parse()[1]

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
            raw_conf["PARAGRAPH_MATH"]
        )

    def conf(self) -> Config:
        """Parse the config of the LaTeX file."""

        raw_conf: dict[str, Any] = self.parse()[0]
        packages: list[str] = raw_conf["PACKAGES"]

        packages[0] = (
                packages[0]
                    .replace("<MARGIN>", f"{raw_conf['MARGIN']}in")
                    .replace("<PAPER_SIZE>", raw_conf["PAPER_SIZE"])
            )
        if raw_conf["COLOR_LINKS"]:
            packages[-1] = packages[-1].replace(
                    "<LINK_COLORS>", raw_conf["LINK_COLORS"].lower()
                )
        else:
            packages.pop(-1)

        return Config(
            raw_conf["DOC_CLASS"],
            raw_conf["DEF_FONT"],
            raw_conf["FONT_SIZE"],
            raw_conf["CODE_FONT"],
            raw_conf["CFONT_SCALE"],
            raw_conf["CODE_CONF"],
            packages,
            raw_conf["SECTION_SIZES"],
            raw_conf["COLOR_LINKS"],
            raw_conf["LINK_COLORS"],
            raw_conf["AUTHOR"],
            raw_conf["DATE"].replace(
                "<NOW>", datetime.now().strftime("%B %d, %Y")
            ),
            raw_conf["MAKE_TITLE"],
            raw_conf["OUTPUT_FOLDER"]
        )
