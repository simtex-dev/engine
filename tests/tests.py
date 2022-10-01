import unittest
from os.path import expanduser

from appdirs import user_config_dir

from src.configs.config import Config
from src.configs.rules import Rules
from src.configs.replacements import Replacements
from src.utils.config_fetch import ConfParse
from src.utils.logger import Logger


class TestCases(unittest.TestCase):
    """Basic test unit for config parse."""

    def setUp(self) -> None:
        self.log: Logger = Logger()
        conf_parser: ConfParse = ConfParse(self.log, True)
        self.config: Config; self.rules: Rules; self.replacement: Replacements
        self.config, self.rules, self.replacement = (
                conf_parser.fetched_conf(assume_yes=True)
            )

    def test_config(self) -> None:
        """Test case for config."""

        self.assertEqual(
            Config(
                doc_class="article",
                doc_font="lmodern",
                font_size=12,
                margin=[1],
                unit="in",
                paper_size="a4paper",
                indent_size=24,
                sloppy=True,
                code_font="DejaVuSansMono",
                cfont_scale=0.9,
                code_conf=(
                        f"{user_config_dir('simtex', 'iaacornus')}"
                        "/code_conf.txt"
                    ),
                packages=[
                    [
                        "geometry",
                        "<MARGIN>, <PAPER_SIZE>"
                    ],
                    "indentfirst",
                    "amsmath",
                    "mathtools",
                    "sectsty",
                    "footmisc",
                    "gensymb",
                    "xcolor",
                    "listings",
                    "caption",
                    "csquotes",
                    [
                        "ulem",
                        "normalem"
                    ],
                    [
                        "hyperref",
                        "colorlinks, allcolors=<LINK_COLORS>"
                    ]
                ],
                footnote="footnote",
                section_sizes={
                        "main": "<DEF>",
                        "sub": "<DEF>",
                        "subsub": "<DEF>"
                    },
                links=True,
                link_color="blue",
                author="John Doe",
                date="<NOW>",
                make_title=True,
                output_folder="out",
                compiler="pdflatex",
                encode="UTF8",
                replace=False,
                twocols=False,
                assume_yes=False
            ),
            self.config
        )

    def test_rules(self) -> None:
        """Test case for rules."""

        self.assertEqual(
            Rules(
                files=[
                        "md"
                    ],
                code="```",
                image="!\\[([^]]+)\\]\\(([^]]+)\\)",
                links="\\[([^]]+)\\]\\(([^]]+)\\)",
                section="#",
                sectionn="#*",
                subsection="##",
                subsectionn="##*",
                subsubsection="###",
                subsubsectionn="###*",
                paragraph="####",
                paragraphn="####*",
                subparagraph="#####",
                subparagraphn="#####*",
                paragraph_math="$$",
                inline_math=["$", "\\$(.*?)\\$"],
                inline_code=["`", "`(.*?)`"],
                bold=["**", "\\*\\*(.*?)\\*\\*"],
                emph=["!*", "!\\*(.*?)!\\*"],
                italics=["__", "__(.*?)__"],
                strike=["~~", "~~(.*?)~~"],
                supscript=["^^", "\\^\\^(.*?)\\^\\^"],
                subscript=["-^", "-\\^(.*?)-\\^"],
                uline=["._", "._(.*?)._"],
                quote=["\"", "\"(.*?)\""],
                bquote=">",
                nonum="*"
            ),
            self.rules
        )

    def test_replacements(self) -> None:
        """Test case for replacements."""

        self.assertEqual(
            Replacements(
                replacements={
                    "-->": "\\longrightarrow",
                    "<--": "\\longleftarrow",
                    "===": "\\equiv",
                    "~==": "\\approxeq",
                    "<<": "\\ll",
                    "<=": "\\leq",
                    ">=": "\\geq",
                    ".=": "\\doteq",
                    "~~": "\\approx",
                    "~=": "\\simeq",
                    "~~=": "\\cong",
                    ">>": "\\gg",
                    "+-": "\\pm",
                    "./.": "\\div",
                    "-+": "\\mp",
                    "|>": "\\triangleleft",
                    "<|": "\\triangleright",
                    "<-": "\\leftarrow",
                    "->": "\\rightarrow",
                    "<->": "\\leftrightarrow",
                    "<==": "\\Leftarrow",
                    "==>": "\\Rightarrow",
                    "<=>": "\\Leftrightarrow",
                    "|->": "\\mapsto",
                    "===>": "\\Longrightarrow",
                    "<===": "\\Longleftarrow",
                    "<===>": "\\Longleftrightarrow",
                    "~~>": "\\leadsto",
                    "...": "\\dots",
                    ":::": "\\vdots",
                    "^...": "\\cdots",
                    "^.": "\\cdots"
                }
            ),
            self.replacement
        )
