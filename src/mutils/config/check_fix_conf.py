from os.path import exists

from src.mutils.config.fetch_missing_conf import fetch_missing_config
from src.utils.logger import Logger


def check_fix_conf(
        log: Logger, CONF_PATH: str, CONF: list[str], assume_yes: bool
    ) -> bool:
    """For checking and fixing the config files of the program.

    Args:
        log -- for instance of Logger.
        CONF_PATH -- path of the config file.
        CONF -- name of the config files to check.
        assumyes -- whether to assume yes or not.
    """

    conf: str
    for conf in CONF:
        MSG: str = (
                f"Cannot find {conf} in PATH"
                ", fetching original config  ..."
            )

        if exists(f"{CONF_PATH}/{conf}"):
            continue

        match conf:
            case "simtex.json":
                fetch_missing_config(
                    log, MSG, CONF_PATH, assume_yes, True
                )
            case "code_conf.txt":
                fetch_missing_config(
                    log, MSG, CONF_PATH, assume_yes, code_conf=True
                )
