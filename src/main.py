from typing import Any, Optional

from src.utils.config import Config, Rules
from src.misc.stdout import Signs
from src.utils.config_fetch import ConfParse
from src.utils.logger import Logger


def main(
        file: Optional[str] = None,
        output: Optional[str] = None,
        title: Optional[str] = None,
        author: Optional[str] = None,
        date: Optional[str] = None,
        font: Optional[str] = None,
        fontsize: Optional[int] = None,
        papersize: Optional[str] = None
    ) -> None:
    """Main program."""

    log: Logger = Logger()
    conf_parse: ConfParse = ConfParse(log)
    config: Config = conf_parse.conf()
    rules: Rules = conf_parse.rules()

    PARAMETERS: dict[str, Any] = {
            "file": file,
            "output": output,
            "title": title,
            "author": author,
            "date": date,
            "font": font,
            "fontsize": fontsize,
            "papersize": papersize
        }

    key_: str; param: Any
    for key_, param in PARAMETERS.items():
        if param is not None:
            print(
                f"{Signs.INFO} {config.__getattribute__(key_)} -> {param}"
            )
            config.__setattr__(key_, param)

