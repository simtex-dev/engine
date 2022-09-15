from argparse import ArgumentParser
from subprocess import CalledProcessError
from typing import Callable

from src.utils.config_fetch import ConfParse
from src.utils.convert import convert
from src.mutils.update_conf import update_conf
from src.metadata.info import PkgInfo
from src.utils.logger import Logger


class Cli:
    """Commandline interface of the program."""

    def __init__(self) -> None:
        self.log: Logger = Logger()
        self.conf_parse: ConfParse = ConfParse(self.log)

        self.parser: ArgumentParser = ArgumentParser(
                prog="simtex",
                usage="simtex [OPTIONS] [INPUT] FILE [ARGUMENTS]",
                description=PkgInfo.__description__
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
            help="Use a different encoding for the document.",
            action="store"
        )
        # self.parser.add_argument(
        #     "-tc", "--twocolumns",
        #     help="Use two columns in the document.",
        #     action="store_true"
        # )

    def _misc(self) -> None:
        """Other arguments."""

        self.parser.add_argument(
            "-ft", "--filenametitle",
            help="Use the filename as title.",
            action="store_true"
        )
        self.parser.add_argument(
            "-v", "--verbose",
            help="Show the stdout of processes.",
            action="store_true"
        )
        self.parser.add_argument(
            "-y", "--assumeyes",
            help="Assume yes to every prompt.",
            action="store_true"
        )
        self.parser.add_argument(
            "-A", "--autocorrect",
            help="Apply autocorrection in wrong spellings.",
            action="store_true"
        )
        self.parser.add_argument(
            "-R", "--replace",
            help="Automatically replace math symbols defined.",
            action="store_true"
        )
        self.parser.add_argument(
            "--version",
            help="Print the version number of the application.",
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

        try:
            if self.args.convert or self.args.build or self.args.buildnview:
                self.config, self.rules, self.replacement = (
                    self.conf_parse.fetched_conf(
                            self.args.assumeyes
                        )
                )

                # update the config for overrides
                update_conf(
                    self.log, self.config, self.args, self.args.assumeyes
                )

                converter: Callable[[], list[str]] = lambda: convert(
                        self.log,
                        self.args,
                        self.rules,
                        self.config,
                        self.replacement
                    )

                files: list[str] = converter()

            elif self.args.version:
                print(f"Simtex version: {PkgInfo.__version__}.")
                raise SystemExit

            else:
                self.log.logger("E", "Unknown option.")

        except KeyboardInterrupt:
            self.log.logger("E", "Operation interrupted, aborting ...")
        except CalledProcessError as Err:
            self.log.logger(
                "E", f"CalledProcessError: {Err}, aborting ..."
            )
        else:
            print(
                f"\033[34mINFO\033[0m\t File(s) {self.args.input} converted "
                f"successfully and can be found in \033[1;36m{files}\033[0m."
            )
