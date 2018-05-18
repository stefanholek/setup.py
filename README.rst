=========
mypackage
=========
------------------------
Another setup.py example
------------------------

This is where I disagree with @kennethreitz' setup.py example. 😎

https://github.com/kennethreitz/setup.py

Issues
====================

1. Code
-------

Setup.py should be as declarative as possible, no unnecessary coding in
setup.py. Ideally, the file only contains a call to setup().

I am always wary of code that is copied around. It is hard to update when
a bug is found or a new Python version needs to be accommodated.

The 'setup.py publish' command contained in the example is not strictly
necessary and can be accomplished with setuptools alone. See point 4 below.

2. Version
----------

You do not want to read the version string from a Python file. In fact it is
the other way round: The version is defined in setup.py and Python code
accesses it via pkg_resources::

    import pkg_resources
    __version__ = pkg_resources.get_distribution('mypackage').version

Note that the version string is normalized by setuptools. It may also be
modified by passing the --tag-build and --tag-date options.

3. setup.cfg
------------

You do not want to skip setup.cfg. Packages are built not only by
you, but also by tools like tox, travis, readthedocs, and even pip.
At least add a section for bdist_wheel::

    [bdist_wheel]
    universal = true

4. Upload
---------

The 'setup.py upload' command is safe to use with recent
versions of Python. See e.g. Python issue12226_ and issue22417_.

If desired, the 'publish' command can be realized as an alias::

    [aliases]
    publish = bdist_wheel upload

.. _issue12226: https://bugs.python.org/issue12226
.. _issue22417: https://bugs.python.org/issue22417

5. Releasers
------------

If you are dealing with more than a handful of packages look into dedicated
software releasers like `jarn.mkrelease`_ and `zest.releaser`_.

.. _`jarn.mkrelease`: https://pypi.org/project/jarn.mkrelease
.. _`zest.releaser`: https://pypi.org/project/zest.releaser

License
=======

This package is in the public domain. The included LICENSE file is part of the
example.
