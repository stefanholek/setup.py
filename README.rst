=========
mypackage
=========
------------------------
Another setup.py example
------------------------

This is where I disagree with aspects of @kennethreitz' setup.py example. 😎

https://github.com/kennethreitz/setup.py

Issues
====================

1. Code
-------

Setup.py should be as declarative as possible, no unnecessary coding in
setup.py. Ideally, the file only contains a call to setup().

I am always wary of code that is "copied around". It is hard to update when
a bug is found or a new Python version needs to be accommodated.

The 'setup.py publish' command contained in the example is not strictly
necessary and can be accomplished with setuptools alone. See point 5. and
setup.cfg_.

2. io.open()
------------

You do not want to use io.open() as it returns Unicode in Python 2. I
suggest this idiom instead::

    import sys, functools
    if sys.version_info >= (3,):
        open = functools.partial(open, encoding='utf-8')

This way file contents will be 'str' type in either version of Python.

3. Version
----------

You do not want to read the version string from a Python file. In fact it is
the other way round: The version is defined in setup.py and Python code
accesses it via pkg_resources::

    import pkg_resources
    __version__ = pkg_resources.get_distribution('mypackage').version

Note that the version string is normalized by setuptools. It may also be
modified by passing the --tag-build and --tag-date options.

4. setup.cfg
------------

You do not want to skip setup.cfg. Packages are built not only by
you, but also by tools like tox, travis, readthedocs, and even pip.

5. Upload
---------

The 'setup.py upload' command is safe to use with recent
versions of Python. See e.g. Python issue12226_ and issue22417_.

.. _setup.cfg: https://github.com/stefanholek/setup.py/blob/master/setup.cfg
.. _issue12226: https://bugs.python.org/issue12226
.. _issue22417: https://bugs.python.org/issue22417

License
=======

This package is in the public domain. The included LICENSE file is part of the
example.
