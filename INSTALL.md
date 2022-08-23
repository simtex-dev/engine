# Installation

# Simple install

The project can be installed using the `.whl` in releases section using your python package manager or using `pip install simtex`, since the project has been on [PyPI](https://pypi.org/project/simtex/) since 0.2.0

## From source

One way to install the project from source is by building it using the build system. Install the dependencies with:

```
pip install -r requirements.txt
```

And using your distro's respective package manager, install texlive or any other LaTeX distributions. In Fedora, CentOS, and RHEL:

```
sudo dnf/rpm-ostree/yum install texlive-scheme-full
```

Then inside the project dir, to build the `.whl` file do:

```
python -m build
```

or to package the project:

```
python setup.py build
```

And finally if the former was used, the resulting `.whl` file under `dists/` dir can be installed via `pip`.
