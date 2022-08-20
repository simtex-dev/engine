from requests import get

from src.utils.logger import Logger


def fix_missing_config(
        log: Logger,
        CONF_PATH: str,
        conf: bool = False,
        code_conf: bool = False
    ) -> None:
    """Downloads the original config file from github if not found.

    Args:
        log -- for logging.
        CONF_PATH -- path of the config file.
        conf, code_conf -- whether the missing config is the code config
            or the main, simtex.json.
    """

    if conf:
        link: str = (
                "https://raw.githubusercontent.com/iaacornus"
                "/simtex/main/examples/config/simtex.json"
            )
        filename: str = "simtex.json"
    elif code_conf:
        link = (
                "https://raw.githubusercontent.com/iaacornus"
                "/simtex/main/examples/config/code_conf.txt"
            )
        filename = "code_conf.txt"

    log.logger(
        "e", f"Config file: {filename} not found, fetching the default."
    )

    for _ in range(3):
        try:
            log.logger(
                "e",
                f"Config file {filename} not found, "
                "fetching original config from GitHub ..."
            )
            with get(link, stream=True) as d_file:
                with open(
                        f"{CONF_PATH}/{filename}", "wb"
                    ) as conf_file:
                    for chunk in d_file.iter_content(chunk_size=1024):
                        if chunk:
                            conf_file.write(chunk)
        except ConnectionError as Err:
            log.logger(
                "E", f"{Err}. Cannot download {filename}, aborting ..."
            )
        else:
            log.logger("I", "Sucessfully fetched the config file.")
            return

    raise SystemExit
