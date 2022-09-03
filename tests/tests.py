import unittest
from os.path import expanduser

from src.config import Config, Replacements, Rules

from src.utils.config_fetch import ConfParse
from src.utils.logger import Logger


class TestCases(unittest.TestCase):
    """Basic test unit for config parse."""

    def setUp(self) -> None:
        self.log: Logger = Logger()
        conf_parser: ConfParse = ConfParse(self.log, True)
        self.config: Config; self.rules: Rules; self.replacement: Replacements
        self.config, self.rules, self.replacement = conf_parser.fetched_conf()

    def test_config(self) -> None:
        """Test case for config."""

        self.assertEqual(
            Config(
                doc_class="article",
                doc_font="lmodern",
                font_size=12,
                margin=1,
                paper_size="a4paper",
                indent_size=24,
                sloppy=True,
                code_font="DejaVuSansMono",
                cfont_scale=0.9,
                code_conf=f"{expanduser('~')}/.config/simtex/code_conf.txt",
                packages=[
                        r"[margin=<MARGIN>, <PAPER_SIZE>]{geometry}",
                        r"{indentfirst}",
                        r"{amsmath}",
                        r"{mathtools}",
                        r"{sectsty}",
                        r"{footmisc}",
                        r"{gensymb}",
                        r"{xcolor}",
                        r"{listings}",
                        r"{caption}",
                        r"{csquotes}",
                        r"[normalem]{ulem}",
                        r"[colorlinks, allcolors=<LINK_COLORS>]{hyperref}"
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
                replace=True
            ),
            self.config
        )

    def test_rules(self) -> None:
        """Test case for rules."""

        self.assertEqual(
            Rules(
                files=[
                        "markdown",
                        "md",
                        "rst",
                        "txt",
                        "text"
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
                bquote=">"
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
