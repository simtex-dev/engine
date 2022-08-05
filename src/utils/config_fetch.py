from os.path import exists, expanduser
from shutil import copy
from json import load
from typing import Any
from datetime import datetime

from src.misc.type_alias import DataTypes
from src.misc.stdout import Signs


class ConfParse:
    def __init__(
            self, log: object, overrides: dict[str, Any] = None
        ) -> None:
        """check the config file in instantiation before proceeding."""

        self.log = log
        self.config_path: str = f"{expanduser('~')}/.config/simtex"
        self.overrides: dict[str, Any] = overrides

        if not exists(f"{self.config_path}/simtex.json"):
            log.logger(
                "E", f"{Signs.INFO} Config file not found, used the default\n"
            )
            copy(
                f"{self.config_path}/simtex.json.bak",
                f"{self.config_path}/simtex.json"
            )

    def parse(self) -> DataTypes.RawConf:
        """parse and replace the overriden parameters in the cli.

        Returns the raw configuration file for further processing.
        """

        with open(
                f"{self.config_path}/simtex.json", "r", encoding="utf-8"
            ) as conf_file:
            conf: dict[str, Any] = load(conf_file)

        if self.overrides is not None:
            for val in self.overrides.keys():
                val: str
                if val in list(conf.keys()):
                    print(
                        f"{Signs.INFO} {conf[val]} -> {self.overrides[val]}"
                    )
                    conf[val] = self.overrides[val]

        return conf

    def conf(self) -> DataTypes.TexConf:
        """finalize the data returned by ConfParse.parse()

        Returns the data ready for use in tex generation.
        """

        raw_conf: DataTypes.RawConf = self.parse()
        packages: DataTypes.TexPkg = raw_conf["PACKAGES"]

        packages[0]: str = (
                packages[0]
                    .replace("<MARGIN>", raw_conf["MARGIN"])
                    .replace("<PAPER_SIZE>", raw_conf["PAPER_SIZE"])
            )
        if raw_conf["COLOR_LINKS"]:
            packages[-1]: str = packages[-1].replace(
                    "<LINK_COLORS>", raw_conf["LINK_COLORS"].lower()
                )
        else:
            packages.pop(-1)

        return (
            raw_conf["DOC_CLASS"],
            raw_conf["DEF_FONT"],
            raw_conf["FONT_SIZE"],
            raw_conf["MAKE_TITLE"],
            packages,
            raw_conf["SECTION_SIZES"],
            raw_conf["AUTHOR"],
            raw_conf["DATE"].replace(
                "<NOW>", datetime.now().strftime("%B %d, %Y")
            )
        )
