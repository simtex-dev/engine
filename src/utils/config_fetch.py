from os.path import exists, expanduser
from shutil import copy
from json import load
from typing import Any

from src.misc.type_alias import DataTypes
from src.misc.signs import Signs


class ConfParse:
    def __init__(self) -> None:
        """check the config file in instantiation before proceeding."""

        self.config_path: str = f"{expanduser('~')}/.config/simtex"

        if not exists(f"{self.config_path}/simtex.json"):
            print(f"{Signs.INFO} Config file not found, used the default\n")
            copy(
                f"{self.config_path}/simtex.json.bak",
                f"{self.config_path}/simtex.json"
            )

    def parse(self, overrides: dict[str, Any]) -> DataTypes.RawConf:
        """parse and replace the overriden parameters in the cli.

        Arguments:
        overrides: dict[str, Any] -- overrides received in cli, will
            replace the fetched items in config file.

        Returns the raw configuration file for further processing.
        """

        with open(
                f"{self.config_path}/simtex.json", "r", encoding="utf-8"
            ) as conf_file:
            conf: dict[str, Any] = load(conf_file)

        for override in overrides.keys():
            override: str
            if overrides in list(conf.keys()):
                print(
                    f"{Signs.INFO} {conf[override]} -> {overrides[override]}"
                )
                conf[override] = overrides[override]

        return conf
