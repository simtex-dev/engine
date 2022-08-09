from os import mkdir
from pathlib import Path
from os.path import exists
from shutil import copy
from json import load
from typing import Any, NoReturn, Optional
from datetime import datetime

from src.misc.config import Config
from src.misc.stdout import Signs


class ConfParse:
    """Parse the JSON configuration file."""

    def __init__(
            self, log: object, overrides: Optional[dict[str, Any]] = None
        ) -> None:
        """check the config file in instantiation before proceeding."""

        self.log = log
        self.BASE_CONF_PATH: str = Path.home()/".config"
        self.CONF_PATH: str = self.BASE_CONF_PATH/"simtex"
        self.overrides: dict[str, Any] = overrides

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

    def parse(self) -> dict[str, Any] | NoReturn:
        """parse and replace the overriden parameters in the cli.

        Returns the raw configuration file for further processing.
        """

        try:
            with open(
                    f"{self.CONF_PATH}/simtex.json",
                    "r",
                    encoding="utf-8"
                ) as conf_file:
                raw_conf: list[dict[str, Any]] = load(conf_file)

            conf = raw_conf[0]
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
            return conf

    def conf(self) -> tuple[Any]:
        """finalize the data returned by ConfParse.parse()

        Returns the data ready for use in tex generation.
        """

        raw_conf: dict[str, Any] = self.parse()
        packages: list[str] = raw_conf["PACKAGES"]

        packages[0]: str = (
                packages[0]
                    .replace("<MARGIN>", f"{raw_conf['MARGIN']}in")
                    .replace("<PAPER_SIZE>", raw_conf["PAPER_SIZE"])
            )
        if raw_conf["COLOR_LINKS"]:
            packages[-1]: str = packages[-1].replace(
                    "<LINK_COLORS>", raw_conf["LINK_COLORS"].lower()
                )
        else:
            packages.pop(-1)

        return Config(
            (
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
        )
