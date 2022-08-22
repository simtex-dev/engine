from argparse import ArgumentParser
from subprocess import CalledProcessError, Popen
from typing import Any, Callable

from src.config import Config, Rules
from src.utils.config_fetch import ConfParse
from src.convert import convert
from src.mutils.build_tex import build_file
from src.mutils.update_conf import update_conf
from src.utils.logger import Logger


class Cli:
    """Commandline interface of the program."""

    def __init__(self) -> None:
        self.log: Logger = Logger()
        conf_parse: ConfParse = ConfParse(self.log)
        self.config: Config = conf_parse.conf()
        self.rules: Rules = conf_parse.rules()

        description: str = (
                "Convert your mardown or text lectures"
                " into LaTeX/pdf with one command.!"
            )
        self.parser: ArgumentParser = ArgumentParser(
                prog="simtex",
                usage="simtex [OPTIONS]",
                description=description
            )

    def _options(self) -> None:
        """The options of the program."""

        self.parser.add_argument( # commands
            "-c", "--convert",
            help="Convert the input to LaTeX.",
            action="store_true"
        )
        self.parser.add_argument(
            "-b", "--build",
            help="Build the generated LaTeX file.",
            action="store_true"
        )
        self.parser.add_argument(
            "-B", "--buildnview",
            help="Build the generated LaTeX file and view the output.",
            action="store_true"
        )

    def _arguments(self) -> None:
        """Main and commonly used arguments of the program"""

        self.parser.add_argument( # starts here are the options
            "-i", "--input",
            help="File to be converted into LaTeX.",
            action="store",
            required=True
        )
        self.parser.add_argument(
            "-T", "--title",
            help="Set the title of the document.",
            action="store",
        )
        self.parser.add_argument(
            "-f", "--filename",
            help="Use different name for the output file.",
            action="store"
        )
        self.parser.add_argument(
            "-of", "--outputfolder",
            help="Change the output folder for the output file.",
            action="store"
        )
        self.parser.add_argument(
            "-a", "--author",
            help="Set the author name of the document.",
            action="store"
        )
        self.parser.add_argument(
            "-d", "--date",
            help="Set the date of the document.",
            action="store"
        )
        self.parser.add_argument(
            "-C", "--compiler",
            help="Use a different LaTeX compiler.",
            action="store"
        )

    def _doc_args(self) -> None:
        """For modification of document properties."""

        self.parser.add_argument(
            "-F", "--font",
            help="Use different font package.",
            action="store"
        )
        self.parser.add_argument(
            "-s", "--fontsize",
            help="Use different font size.",
            action="store"
        )
        self.parser.add_argument(
            "-p", "--papersize",
            help="Use different paper size.",
            action="store"
        )
        self.parser.add_argument(
            "-I", "--indent",
            help="Indent size to be used.",
            action="store"
        )
        self.parser.add_argument(
            "-m", "--margin",
            help="Margin size to be used.",
            action="store"
        )
        self.parser.add_argument(
            "-e", "--encoding",
            help="Use a different encoding for document.",
            action="store"
        )

    def _misc(self) -> None:
        """Other arguments."""

        self.parser.add_argument(
            "-ft", "--filenametitle",
            help="Use the filename as title.",
            action="store_true"
        )
        self.parser.add_argument(
            "-v", "--verbose",
            help="Hide stdout of other processes.",
            action="store_true"
        )

    def create_parser(self) -> None:
        """Create the parser."""

        self._options()
        self._doc_args()
        self._arguments()
        self._misc()

        self.args = self.parser.parse_args()

    def cli(self) -> None:
        """Commandline interface of the program."""

        self.create_parser() # create the arguments
        # update the config for overrides
        update_conf(self.log, self.config, self.args)

        converter: Callable[..., Any] = lambda: convert(
                self.log,
                self.rules,
                self.config,
                self.args.title,
                self.args.input,
                self.args.filenametitle
            )

        try:
            if self.args.convert:
                converter()
            elif self.args.build:
                converter()
                build_file(
                    self.log,
                    self.config.compiler,
                    self.config.output_folder,
                    self.config.filename,
                    self.args.verbose
                )
            elif self.args.buildnview:
                converter()
                build_file(
                    self.log,
                    self.config.compiler,
                    self.config.output_folder,
                    self.config.filename,
                    self.args.verbose
                )
                try:
                    Popen(["xgd-open", self.args.filename])
                except FileNotFoundError:
                    self.log.logger(
                        "e", "No PDF viewer found, cannot view PDF file."
                    )
            else:
                self.log.logger("E", "Unknown option.")
        except KeyboardInterrupt:
            self.log.logger("E", "Operation interrupted, aborting ...")
        except CalledProcessError as Err:
            self.log.logger(
                "E", f"CalledProcessError: {Err}, aborting ..."
            )
