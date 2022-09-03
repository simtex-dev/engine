from os import mkdir
from os.path import exists, expanduser
from pathlib import Path
from json import JSONDecodeError, load
from typing import IO, Any, NoReturn, Optional

from src.config import Config, Rules, Replacements
from src.mutils.fix_missing_conf import fix_missing_config
from src.utils.logger import Logger


class ConfParse:
    """Parse the JSON configuration file."""

    def __init__(self, log: Logger, test: Optional[bool] = False) -> None:
        """Check the config file in instantiation before proceeding.

        Args:
            log -- for logging.
            test -- to know if the execution is for unit testing.
        """

        self.log: Logger = log
        self.HOME: Path = Path.home()
        self.BASE_CONF_PATH: str = f"{self.HOME}/.config"
        self.CONF_PATH: str = (
                (
                    f"{self.BASE_CONF_PATH}/simtex"
                ) if not test else (
                    "./examples/config"
                )
            )

        paths: str
        for paths in [self.BASE_CONF_PATH, self.CONF_PATH]:
            if not exists(paths):
                try:
                    mkdir(paths)
                except (SystemError, OSError, IOError) as Err:
                    self.log.logger(
                        "E", f"{Err}. Cannot create: {paths}, aborting ..."
                    )
                    raise SystemExit

        if not exists(f"{self.CONF_PATH}/simtex.json"):
            fix_missing_config(
                self.log,
                (
                    "Cannot find simtex.json in PATH"
                    ", fetching original config  ..."
                ),
                self.CONF_PATH,
                True
            )
        elif not exists(f"{self.CONF_PATH}/code_conf.txt"):
            fix_missing_config(
                self.log,
                (
                    "Cannot find code_conf.txt in PATH"
                    ", fetching original config  ..."
                ),
                self.CONF_PATH,
                True
            )

    def _fetch(self) -> list[dict[str, Any]] | NoReturn:
        """Fetch the values from config file.

        Returns:
            The list of all values found in the defined array in JSON
            config file.
        """

        try:
            conf_file: IO[Any]
            with open(
                    f"{self.CONF_PATH}/simtex.json",
                    "r",
                    encoding="utf-8"
                ) as conf_file:
                raw_conf: list[dict[str, Any]] = load(conf_file)
        except (
                FileNotFoundError,
                PermissionError,
                JSONDecodeError
            ) as Err:
            self.log.logger(
                "E", f"{Err}. Cannot fetch config file, aborting ..."
            )
            raise SystemExit

        return raw_conf

    def _rules(self) -> Rules:
        """Parse the config of the rules of converter.

        Returns:
            The dataclass of rules with updated values.
        """

        raw_conf: dict[str, Any] = self.raw_conf_[0]

        return Rules(
            raw_conf["FOR"],
            raw_conf["CODE_BLOCKS"],
            raw_conf["IMAGE"],
            raw_conf["LINKS"],
            raw_conf["SECTION"],
            f"{raw_conf['SECTION']}*",
            raw_conf["SUBSECTION"],
            f"{raw_conf['SUBSECTION']}*",
            raw_conf["SUBSUBSECTION"],
            f"{raw_conf['SUBSUBSECTION']}*",
            raw_conf["PARAGRAPH"],
            f"{raw_conf['PARAGRAPH']}*",
            raw_conf["SUBPARAGRAPH"],
            f"{raw_conf['SUBPARAGRAPH']}*",
            raw_conf["PARAGRAPH_MATH"],
            raw_conf["INLINE_MATH"],
            raw_conf["INLINE_CODE"],
            raw_conf["BOLD"],
            raw_conf["ITALICS"],
            raw_conf["EMPH"],
            raw_conf["STRIKE"],
            raw_conf["SUPSCRIPT"],
            raw_conf["SUBSCRIPT"],
            raw_conf["ULINE"],
            raw_conf["QUOTE"],
            raw_conf["BQUOTE"]
        )

    def _conf(self) -> Config:
        """Parse the config of the LaTeX file.

        Returns:
            The dataclass of config with update values.
        """

        raw_conf: dict[str, Any] = self.raw_conf_[1]

        return Config(
            raw_conf["DOC_CLASS"],
            raw_conf["DEF_FONT"],
            raw_conf["FONT_SIZE"],
            raw_conf["MARGIN"],
            raw_conf["PAPER_SIZE"],
            raw_conf["INDENT_SIZE"],
            raw_conf["SLOPPY"],
            raw_conf["CODE_FONT"],
            raw_conf["CFONT_SCALE"],
            raw_conf["CODE_CONF"].replace(
                "<HOME>", expanduser("~")
            ),
            raw_conf["PACKAGES"],
            raw_conf["FOOTNOTE"],
            raw_conf["SECTION_SIZES"],
            raw_conf["LINKS"],
            raw_conf["LINK_COLOR"],
            raw_conf["AUTHOR"],
            raw_conf["DATE"],
            raw_conf["MAKE_TITLE"],
            raw_conf["OUTPUT_FOLDER"],
            raw_conf["COMPILER"],
            raw_conf["ENCODE"],
            raw_conf["REPLACE"]
        )

    def _replacements(self) -> Replacements:
        """Fetch the data of the replacements for some math symbols
        defined in the config file.

        Returns:
            The updated dataclass with the data of the replacements.
        """

        raw_conf: dict[str, Any] = self.raw_conf_[2]

        return Replacements(raw_conf)

    def fetched_conf(self) -> tuple[Config, Rules, Replacements] | NoReturn:
        """Fetch the values from config file, and give fallback method
        for its respective function.

        Returns:
            Both of the parsed data from the raw JSON config file.
        """

        for _ in range(3):
            try:
                self.raw_conf_ = self._fetch()
                config_values: Config = self._conf()
                rules_values: Rules = self._rules()
                replacements: Replacements = self._replacements()
            except KeyError as Err:
                fix_missing_config(
                    self.log,
                    (
                        f"Missing {Err}. Some parameters are missing,"
                        f" fetching the new config file from development ..."
                    ),
                    self.CONF_PATH,
                    conf=True,
                    missing=False
                )
                continue
            else:
                return config_values, rules_values, replacements

        self.log.logger(
            "E", "There is an error with in the config file, aborting ..."
        )
        raise SystemExit
