from setuptools import setup
from os import walk
from os.path import join
from typing import TextIO


def find_module(PATH: str = "src") -> list[str]:
    """Find modules in the given path.

    Args:
        PATH -- where to look from.

    Returns:
        The list of all modules found.
    """

    modules: list[str] = []

    root: str; dir: str | list[str]
    for root, _, dir in walk(PATH):
        for file in dir:
            if file.endswith(".py") and not file.endswith("__init__.py"):
                modules.append(join(root, file).removesuffix(".py"))

    return modules


desc: TextIO
with open("README.md", "r", encoding="utf-8") as desc:
    readme: str = desc.read()

setup(
    name="simtex",
    version="0.3.3.1-beta",
    description=(
            "Convert your markdown or text files"
            " into LaTeX/pdf with one command!"
        ),
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/iaacornus/simtex",
    author="iaacornus",
    author_email="iaacornus.devel@gmail.com",
    license="GPL v3",
    py_modules=find_module(),
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

