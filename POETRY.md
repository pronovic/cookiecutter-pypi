## Installing Poetry

Nearly all prerequisites are managed by Poetry.  All you need to do is make
sure that you have a working Python 3 enviroment and install Poetry itself.

### Poetry Version

The project is designed to work with Poetry >= 2.0.0.  If you already have an older
version of Poetry installed on your system, upgrade it first.

### MacOS

On MacOS, it's easiest to use [Homebrew](https://brew.sh/) to install Python and pipx:

```
brew install python3 pipx
```

Once that's done, make sure the `python` on your `$PATH` is Python 3 from
Homebrew (in `/usr/local`), rather than the standard Python 2 that comes with
older versions of MacOS.

Finally, install Poetry itself:

```
pipx install poetry
```

To upgrade this installation later, use:

```
pipx upgrade poetry
```

### Debian

First, install Python 3 and related tools:

```
sudo apt-get install python3 python-is-python3 pipx
```

Once that's done, make sure that the `python` interpreter on your `$PATH` is
Python 3.

Finally, install Poetry itself:

```
pipx install poetry
```

To upgrade this installation later, use:

```
pipx upgrade poetry
```

### Windows

First, install Python 3 from your preferred source, either a standard
installer or a meta-installer like Chocolatey.  Make sure the `python`
on your `$PATH` is Python 3.

Next, install pipx:

```
python -m pip install --user pipx
```

Finally, install Poetry itself:

```
pipx install poetry
```

To upgrade this installation later, use:

```
pipx upgrade poetry
```

> _Note:_ The development environment (the `run` script, etc.) expects a bash
> shell to be available.  On Windows, it works fine with the standard Git Bash.
