# Installation

# Simple install

Since `v0.3.2-beta`, there is a [built program released](https://github.com/iaacornus/simtex/releases/download/v0.3.2-beta/simtex)
which can be simply just downloaded and executed with `./simtex [OPTIONS]`,
as all of the dependency as well as run time is already included.

After downloading, the program can be placed in your `$PATH` that it can be
easily called. Usually the `$PATH` is `$HOME./local/bin`.

Another method to install the program is using the `.whl` in releases section using your python
package manager or using `pip install simtex`, since the project has been on
[PyPI](https://pypi.org/project/simtex/) since `v0.2.0-alpha`.

## From source

One way to install the project from source is by building it using the build system. Install the dependencies with:

```
pip install -r requirements.txt
```

And using your distro's respective package manager, install texlive or any other
LaTeX distributions. In Fedora, CentOS, and RHEL:

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

And finally if the former was used, the resulting `.whl` file under
`dists/` dir can be installed via `pip`.
