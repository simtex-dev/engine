from os.path import exists, expanduser
from shutil import copy
from json import load
from typing import Any

from src.misc.type_alias import DataTypes
from src.misc.signs import Signs


class ConfParse:
    def __init__(self, overrides: dict[str, Any]) -> None:
        """check the config file in instantiation before proceeding."""

        self.config_path: str = f"{expanduser('~')}/.config/simtex"
        self.overrides: dict[str, Any] = overrides

        if not exists(f"{self.config_path}/simtex.json"):
            print(f"{Signs.INFO} Config file not found, used the default\n")
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

        for val in self.overrides.keys():
            val: str
            if val in list(conf.keys()):
                print(
                    f"{Signs.INFO} {conf[val]} -> {self.overrides[val]}"
                )
                conf[val] = self.overrides[val]

        return conf
