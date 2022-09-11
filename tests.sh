#!/usr/bin/env bash

if [[ ! $(command -v python &> /dev/null) ]]; then
    python="python"
else
    python="python3.10"
fi


if [[ ! $(command -v mypy --help &> /dev/null) ]]; then
    python -m pip install mypy
fi

if [[ ! $(command -v pytest --help &> /dev/null) ]]; then
    python -m pip install pyinstaller
fi

pip install -r mypy_requirements.txt
python -m pytest tests/tests.py
mypy --strict  $(git ls-files "*.py")
