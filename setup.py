from setuptools import setup
from typing import TextIO


desc: TextIO
with open("README.md", "r", encoding="utf-8") as desc:
    readme: str = desc.read()

setup(
    name="simtex",
    version="v0.2.0-alpha",
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
            "src/convert",
            "src/config",
            "src/utils/tex/sections/body",
            "src/utils/tex/sections/headings",
            "src/utils/config_fetch",
            "src/utils/logger",
            "src/mutils/functions",
            "src/misc/stdout"
        ],
    python_requires=">=3.10",
    install_requires=[
            "rich==12.4.4",
            "requests==2.28.1"
        ],
    classifiers=[
            "Development Status :: 3 - Alpha",
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
