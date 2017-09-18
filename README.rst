=========
mypackage
=========
------------------------
Another example setup.py
------------------------

This is where I disagree with aspects of @kennethreitz' setup.py example. 😎

Improvements
============

1. Setup.py should be as declarative as possible, no unnecessary coding in
   setup.py.

2. You do not want to use io.open() as it returns Unicode in Python 2. I
   suggest this idiom instead::

    import sys, functools
    if sys.version_info >= (3,):
        open = functools.partial(open, encoding='utf-8')

3. You do not want to read the version string from a Python file. In fact it is
   the other way round: The version is defined in setup.py and Python code
   accesses it via pkg_resources::

    import pkg_resources
    __version__ = pkg_resources.get_distribution('mypackage').version

4. You do not want to skip setup.cfg. Packages are built not only by
   you, but also by tools like tox, travis, readthedocs, and even pip.

5. Contrary to popular believe, ``setup.py upload`` is safe to use in recent
   versions of Python.
   See e.g. https://bugs.python.org/issue12226.

6. The package should contain a test suite, tox configuration, and a changelog.
