from setuptools import setup
from os import walk
from os.path import join
from typing import TextIO

from src.metadata.info import PkgInfo


def find_module(PATH: str) -> list[str]:
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


def get_dependencies(source: str) -> list[str]:
    """Get the listed dependencies in requirements.txt

    Args:
        source -- requirements.txt

    Returns:
        The list of dependencies.
    """

    try:
        dep_list: TextIO
        with open(source, "r", encoding="utf-8") as dep_list:
            deps: list[str] = dep_list.readlines()
    except FileNotFoundError as Err:
        raise SystemExit("Cannot fetch dependencies.")

    return [
        dep.replace("\n", "") for dep in deps if dep not in ["", "\n"]
    ]


desc: TextIO
with open("README.md", "r", encoding="utf-8") as desc:
    readme: str = desc.read()

setup(
    name="simtex",
    version=PkgInfo.__version__,
    description=PkgInfo.__description__,
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/iaacornus/simtex",
    author=PkgInfo.__author__,
    author_email=PkgInfo.__author_email__,
    maintainer=PkgInfo.__author__,
    maintainer_email=PkgInfo.__author_email__,
    license="GPL v3",
    py_modules=find_module("src"),
    python_requires=">=3.10",
    install_requires=get_dependencies("requirements.txt"),
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
