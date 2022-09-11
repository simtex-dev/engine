from setuptools import setup
from typing import TextIO

from setup_utils import get_dependencies, find_module


desc: TextIO
with open("README.md", "r", encoding="utf-8") as desc:
    readme: str = desc.read()

setup(
    name="simtex",
    version="0.4-beta",
    description=(
            "Convert your markdown or text files"
            " into LaTeX/pdf with one command!\n"
            "Interop with LaTeX and markdown is "
            "also allowed by simtex!"
        ),
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/iaacornus/simtex",
    author="James Aaron Erang (iaacornus)",
    author_email="iaacornus.devel@gmail.com",
    maintainer="James Aaron Erang (iaacornus)",
    maintainer_email="iaacornus.devel@gmail.com",
    license="GPL v3",
    py_modules=find_module(),
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


