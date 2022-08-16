from setuptools import setup, find_packages
from typing import TextIO


desc: TextIO
with open("README.md", "r", encoding="utf-8") as desc:
    readme: str = desc.read()


setup(
    name="simtex",
    version="v0.1.0a",
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
            "main",
            "cli",
            "convert",
            "config",
            "utils/tex/sections/body",
            "utils/tex/sections/headings",
            "utils/config_fetch",
            "utils/logger",
            "mutils/functions",
            "misc/stdout"
        ],
    package_dir={
            "": "src"
        },
    packages=find_packages(
            where="src",
            include=[
                    "misc",
                    "mutils",
                    "utils",
                    "utils/tex",
                    "utils/tex/sections"
                ]
        ),
    python_requires=">=3.10",
    install_requires=[
            "rich==12.4.4",
            "requests==2.28.1"
        ],
    classifiers=[
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3.10",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
            "Intended Audience :: End Users/Desktop",
            "Natural Language :: English",
            "Operating System :: OS Independent",
        ],
    entry_points={
        "console_scripts" : [
            "simtex=main:main",
        ]
    },
)
