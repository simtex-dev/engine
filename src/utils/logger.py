import logging
from pathlib import Path
from os import mkdir
from os.path import exists

from rich.logging import RichHandler

from src.misc.stdout import Signs


class Logger:
    """Custom logger."""

    def __init__(self) -> None:
        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            datefmt="[%X]",
            handlers=[RichHandler()]
        )
        RichHandler.KEYWORDS = [
                "[ PROC ]",
                "[ INPT ]",
                "[ FAIL ]",
            ]
        self.log: object = logging.getLogger("rich")

        BASE_PATH: str = Path.home()/".simtex"
        if not exists(BASE_PATH):
            try:
                mkdir(BASE_PATH)
            except (PermissionError, OSError, IOError) as Err:
                self.logger(
                    "E", f"Cannot create directory: {Err}, aborting ..."
                )

        file_log: object = logging.FileHandler(
                filename=f"{BASE_PATH}/simtex.log"
            )

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(
            logging.Formatter("%(levelname)s %(message)s")
        )
        self.log.addHandler(file_log)

    def logger(self, exception_: str, message: str) -> None:
        """Log the proccesses using passed message and exception_ variable.

        Arguments:
        exception_: str -- determines what type of log level to use
        message: str -- message to be logged.
        """

        match exception_:
            case "E": # for major error
                self.log.error("%s %s" % (Signs.FAIL, message))
            case "P": # for major processes
                self.log.info("%s %s" % (Signs.PROC, message))
            case "I": # to print information in the terminal
                self.log.info("%s %s" % (Signs.INFO, message))
