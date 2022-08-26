from json import JSONDecodeError, load, dump
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
        conf: list[dict[str, Any]] = []

        _new_conf: TextIO; _conf_ref: TextIO;
        with open(
                f"{CONF_PATH}/simtex.json.bak", "r", encoding="utf-8"
            ) as _new_conf, open(
                f"{CONF_PATH}/simtex.json", "r", encoding="utf-8"
            ) as _conf_ref:
            new_conf_: dict[str, Any] = load(_new_conf)
            conf_ref_: dict[str, Any] = load(_conf_ref)

        param: str; new_val: Any; old_conf: Any; new_conf: Any
        for old_conf, new_conf in zip(
                [ref for ref in conf_ref_], [new for new in new_conf_]
            ):
            temp_conf: dict[str, Any] = {}

            for param, new_val in new_conf.items():
                temp_conf[param] = old_conf.get(param, new_val)
            conf.append(temp_conf)

        fixed_conf: TextIO
        with open(
                f"{CONF_PATH}/simtex.json", "w", encoding="utf-8"
            ) as fixed_conf:
            dump(conf, fixed_conf, indent=4)
    except (FileNotFoundError, IOError, JSONDecodeError) as Err:
        log.logger(
            "e", f"{Err}. Cannot merge the two config files, skipping ..."
        )
