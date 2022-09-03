import logging
from pathlib import Path
from os import mkdir
from os.path import exists

from rich.logging import RichHandler


class Logger:
    """Custom logger."""

    def __init__(self) -> None:
        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            datefmt="[%X]",
            handlers=[
                    RichHandler(
                        show_time=False,
                        show_path=False
                    )
                ]
        )

        self.log: logging.Logger = logging.getLogger("rich")

        BASE_PATH: Path = Path.home()/".simtex"
        if not exists(BASE_PATH):
            try:
                mkdir(BASE_PATH)
            except (PermissionError, OSError, IOError) as Err:
                self.logger(
                    "E", f"Cannot create directory: {Err}, aborting ..."
                )

        file_log: logging.FileHandler = logging.FileHandler(
                filename=f"{BASE_PATH}/simtex.log"
            )

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(
            logging.Formatter("%(levelname)s %(message)s")
        )
        self.log.addHandler(file_log)

    def logger(self, exception_: str, message: str) -> None:
        """Log the proccesses using passed message and exception_ variable.

        Args:
            exception_ -- determines what type of log level to use
            message -- message to be logged.
        """

        match exception_:
            case "E": # for major error
                self.log.critical("%s" % (message))
            case "e":
                self.log.error("%s" % (message))
            case "I": # to print information in the terminal
                self.log.info("%s" % (message))
