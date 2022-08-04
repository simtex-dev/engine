import logging
from typing import Optional
from os.path import expanduser

from rich.logging import RichHandler

from src.misc.signs import Signs


class Logger:
    """Custom logger."""

    def __init__(self, filename: Optional[str] = None) -> None:
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

        if filename is None:
            file_log: object = logging.FileHandler(filename=filename)
        else:
            file_log: object = logging.FileHandler(
                filename=f"{expanduser('~')}/.simtex/simtex.log"
            )

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(
            logging.Formatter("%(levelname)s %(message)s")
        )
        self.log.addHandler(file_log)

    def logger(self, exception_: str, message: str) -> None:
        """Log the proccesses using passed message and exception_ variable.

        Arguments:
        exception_: str, determines what type of log level to use
            (a.) "error" for major error that crashed the program
            (b.) "Finfo" for failed subprocesses
            (c.) "subinfo" to simply log the happening subprocesses
            (d.) "proc_info" for major processes
            (e.) "info" for information about the process
        message: str, message to be logged.
        """

        match exception_:
            case "E": # for major error
                self.log.error("%s %s" % (Signs.FAIL, message))
            case "P": # for major processes
                self.log.info("%s %s" % (Signs.PROC, message))
            case "I": # to print information in the terminal
                self.log.info("%s %s" % (Signs.INFO, message))
