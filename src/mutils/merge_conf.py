from json import load
from typing import Any, TextIO

from src.utils.logger import Logger


def merge_conf(log: Logger, conf_path: str) -> None:
    """When fixing the two config files due to missing parameter, the
    other parameters should not be overwritten by the default config
    that will be fetched from the repository, thus the two should be
    merged instead."""

    try:
        temp_conf: dict[str, Any] = {}

        conf_ref: TextIO; conf: TextIO;
        with open(
                f"{conf_path}/simtex.json.bak", "r", encoding="utf-8"
            ) as conf_ref, open(
                f"{conf_path}/simtex.json", "r", encoding="utf-8"
            ) as conf:
            conf: dict[str, Any] = load(conf)
            conf_ref: dict[str, Any] = load(conf_ref)

    except FileNotFoundError as Err:
        log.logger(
            "e", f"{Err}. Cannot merge the two config files, skipping ..."
        )
