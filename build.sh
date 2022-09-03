if [[ ! $(command -v python &> /dev/null) ]]; then 
    python="python3.10"
else
    python="python"
fi

if [[ ! $(command -v pyinstaller &> /dev/null) ]]; then
    python -m pip install pyinstaller
fi

pyinstaller src/main.py --name simtex --onefile -y


