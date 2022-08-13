from typing import Any

from src.utils.config import Config, Rules
from src.misc.stdout import Signs
from src.utils.config_fetch import ConfParse
from src.utils.logger import Logger
from src.utils.tex.sections.headings import headings
from src.utils.tex.sections.body import body, format_body


def main(
        file: str = None,
        output: str = None,
        title: str = None,
        author: str = None,
        date: str = None,
        font: str = None,
        fontsize: int = None,
        papersize: str = None
    ) -> None:
    """Main program."""

    log: Logger = Logger()
    conf_parse: ConfParse = ConfParse(log)
    config: Config = conf_parse.parse()
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

