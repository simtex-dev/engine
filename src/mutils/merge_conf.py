from json import load, dump
from typing import Any, TextIO

from src.utils.logger import Logger


def merge_conf(log: Logger, CONF_PATH: str) -> None:
    """When fixing the two config files due to missing parameter, the
    other parameters should not be overwritten by the default config
    that will be fetched from the repository, thus the two should be
    merged instead.

    Args:
        log -- for logging.
        CONF_PATH -- path of the config file.
    """

    try:
        # in this context, Any type hint implies the value is either
        #   int, list[Any], float, dict[str, Any].
        temp_conf: dict[str, Any] = {}

        new_conf: TextIO; conf_ref: TextIO;
        with open(
                f"{CONF_PATH}/simtex.json.bak", "r", encoding="utf-8"
            ) as new_conf, open(
                f"{CONF_PATH}/simtex.json", "r", encoding="utf-8"
            ) as conf_ref:
            conf_ref_: dict[str, Any] = load(conf_ref)
            new_conf_: dict[str, Any] = load(new_conf)

        param: str; new_val: Any; conf_val: Any
        for old_conf, new_conf in zip(
                [ref for ref in conf_ref_], [new for new in new_conf_]
            ):
            for param, new_val in new_conf.items():
                if (conf_val := old_conf.get(param, new_val)) != new_val:
                    temp_conf[param] = conf_val
                else:
                    temp_conf[param] = new_val

        print(temp_conf)
        fixed_conf: TextIO
        with open(
                f"{CONF_PATH}/simtex.json", "w", encoding="utf-8"
            ) as fixed_conf:
            dump(temp_conf, fixed_conf, indent=4)
    except FileNotFoundError as Err:
        log.logger(
            "e", f"{Err}. Cannot merge the two config files, skipping ..."
        )
