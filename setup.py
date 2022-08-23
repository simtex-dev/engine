from setuptools import setup
from typing import TextIO


desc: TextIO
with open("README.md", "r", encoding="utf-8") as desc:
    readme: str = desc.read()

setup(
    name="simtex",
    version="v0.3.0-beta",
    description=(
            "Convert your mardown or text lectures"
            " into LaTeX/pdf with one command."
        ),
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/iaacornus/simtex",
    author="iaacornus",
    author_email="iaacornus.devel@gmail.com",
    license="GPL v3",
    py_modules=[
            "src/main",
            "src/cli",
            "src/config",
            "src/convert",
            "src/utils/config_fetch",
            "src/utils/logger",
            "src/utils/tex/environments/figure",
            "src/utils/tex/environments/mathsec",
            "src/utils/tex/environments/quotes",
            "src/utils/tex/environments/listings",
            "src/utils/tex/parser/body",
            "src/utils/tex/parser/headings",
            "src/utils/tex/text/format",
            "src/mutils/build_tex",
            "src/mutils/fix_missing_conf",
            "src/mutils/format_body",
            "src/mutils/update_conf",
            "src/mutils/finalize",
            "src/mutils/preparation"
        ],
    python_requires=">=3.10",
    install_requires=[
            "rich==12.4.4",
            "requests==2.28.1"
        ],
    classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3.10",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
        ],
    entry_points={
        "console_scripts" : [
            "simtex=src.main:main",
        ]
    },
)
