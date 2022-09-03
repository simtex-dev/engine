#!/usr/bin/env bash

if [[ ! $(command -v python &> /dev/null) ]]; then 
    python="python3.10"
else
    python="python"
fi

if [[ ! $(command -v pyinstaller &> /dev/null) ]]; then
    python -m pip install pyinstaller
fi

pip install -r requirements.txt
pip install setuptools build
pyinstaller src/main.py --name simtex --onefile -y
python setup.py sdist
python -m build
