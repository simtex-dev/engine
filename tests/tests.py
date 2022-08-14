import unittest

from src.utils.config import Config, Rules

from src.utils.config_fetch import ConfParse
from src.utils.logger import Logger


class TestCases(unittest.TestCase):
    """Basic test unit for config parse."""

    def setUp(self) -> None:
        self.log: Logger = Logger()
        self.config: ConfParse = ConfParse(self.log, True)

    def test_config(self) -> None:
        """Test case for config."""

        conf: Config = self.config.conf()

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
                code_conf="./examples/config/code_conf.txt",
                packages=[
                        "[margin=<MARGIN>, <PAPER_SIZE>]{geometry}",
                        "{indentfirst}",
                        "{amsmath}",
                        "{mathtools}",
                        "{sectsty}",
                        "{footmisc}",
                        "{gensymb}",
                        "{xcolor}",
                        "{listings}",
                        "{caption}",
                        "[colorlinks, allcolors=<LINK_COLORS>]{hyperref}"
                    ],
                footnote="footnote",
                section_sizes={
                        "main": 12,
                        "sub": 12,
                        "subsub": 12
                    },
                links=True,
                link_color="blue",
                author="John Doe",
                date="<NOW>",
                make_title=True,
                filename="a.tex",
                output_folder="./out/"
            ),
            conf
        )

    def test_rules(self) -> None:
        """Test case for rules."""

        rules: Rules = self.config.rules()

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
                subsection="##",
                subsubsection="###",
                paragraph="####",
                subparagraph="#####",
                inline_math="$",
                paragraph_math="$$",
                inline_code="`(.*?)`"
            ),
            rules
        )
