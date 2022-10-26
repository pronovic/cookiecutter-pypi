## Installing Poetry

Nearly all prerequisites are managed by Poetry.  All you need to do is make
sure that you have a working Python 3 enviroment and install Poetry itself.

### Poetry Version

The project is designed to work with Poetry >= 1.2.0.  If you already have an older
version of Poetry installed on your system, uninstall it before following the setup
process below:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - --uninstall
```

See the [Announcing Poetry 1.2.0](https://python-poetry.org/blog/announcing-poetry-1.2.0/)
blog post for more information.

### MacOS

On MacOS, it's easiest to use [Homebrew](https://brew.sh/) to install Python:

```
brew install python3
```

Once that's done, make sure the `python` on your `$PATH` is Python 3 from
Homebrew (in `/usr/local`), rather than the standard Python 2 that comes with
MacOS.

Although Poetry can also be installed from Homebrew, it works better to use
to [official installer](https://python-poetry.org/docs/#installing-with-the-official-installer):

```
curl -sSL https://install.python-poetry.org | python3 -
```

> _Note:_ The installer prints the location of the installed `poetry` script.
> Make sure to add this to your `$PATH`, otherwise you won't be able to run it.

### Debian

First, install Python 3 and related tools:

```
sudo apt-get install python3 python3-venv python3-pip
```

Next, make sure that the `python` interpreter on your `$PATH` is Python 3.

If you are using Debian _bullseye_ or later (first released in August 2021),
then Python 2 is deprecated and Python 3 is the primary Python on your system.
However, by default there is only a `python3` interpreter on your `$PATH`, not
a `python` interpreter.  To add the `python` interpreter, use:

```
sudo apt-get install python-is-python3
```

For earlier releases of Debian where both Python 2 and Python 3 are available,
the process is a little more complicated.  The approach I used before upgrading
to _bullseye_ was based on `update-alternatives`, as discussed on
[StackExchange](https://unix.stackexchange.com/a/410851).

Next, install Poetry using the [official installer](https://python-poetry.org/docs/#installing-with-the-official-installer):

```
curl -sSL https://install.python-poetry.org | python3 -
```

> _Note:_ The installer prints the location of the installed `poetry` script.
> Make sure to add this to your `$PATH`, otherwise you won't be able to run it.

### Windows

First, install Python 3 from your preferred source, either a standard
installer or a meta-installer like Chocolatey.  Make sure the `python`
on your `$PATH` is Python 3.

Next, install Poetry using the [official installer](https://python-poetry.org/docs/#installing-with-the-official-installer):

```
curl -sSL https://install.python-poetry.org | python -
```

> _Note:_ The installer prints the location of the installed `poetry` script.
> Make sure to add this to your `$PATH`, otherwise you won't be able to run it.

The development environment (the `run` script, etc.) expects a bash shell
to be available.  On Windows, it works fine with the standard Git Bash.
