Example Python Package
==============================================================================

September 2023

Contents
==============================================================================

pyproject.toml
------------------------------------------------------------------------------

Specifies the environment in which sdist and wheel distributions are built.

.. code:: toml

    [build-system]
    requires = ["setuptools", "wheel"]
    build-backend = "setuptools.build_meta"

https://setuptools.pypa.io/en/latest/build_meta.html

setup.cfg
------------------------------------------------------------------------------

Contains configuration required to build "mypackage" with the setuptools backend.

.. code:: ini

    [metadata]
    name = mypackage
    version = attr: mypackage.__version__
    description = My description
    long_description = file: README.rst, CHANGES.rst
    long_description_content_type = text/x-rst
    classifiers =
        Development Status :: 5 - Production/Stable
        License :: OSI Approved :: BSD License
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 3
    keywords = my, package, keywords
    author = My Name
    author_email = me@example.com
    url = https://github.com/me/mypackage
    project_urls =
        Documentation = https://mypackage.readthedocs.io/en/stable/
    license = BSD-2-Clause

    [options]
    packages = find:
    include_package_data = false
    zip_safe = false
    install_requires =
        setuptools
    python_requires = >=3.7

    [options.packages.find]
    exclude =
        tests

    [options.entry_points]
    console_scripts =
        myscript = mypackage.mypackage:main

    [options.extras_require]
    docs =
        sphinx
        sphinx-rtd-theme

https://setuptools.pypa.io/en/latest/userguide/declarative_config.html

setup.py
------------------------------------------------------------------------------

Almost empty now but still needed for at least the develop command
(pip install -e).

.. code:: python

    from setuptools import setup

    setup()

https://setuptools.pypa.io/en/latest/userguide/commands.html

MANIFEST.in
------------------------------------------------------------------------------

Controls which files end up in the sdist. Note that we include tests here.

.. code::

    include LICENSE tox.ini *.rst
    recursive-include tests *.py

https://setuptools.pypa.io/en/latest/deprecated/distutils/sourcedist.html#manifest

LICENSE
------------------------------------------------------------------------------

BSD 2-Clause by default. Feel free to use your favorite license instead.

https://choosealicense.com/licenses/

README.rst
------------------------------------------------------------------------------

Readme.

CHANGES.rst
------------------------------------------------------------------------------

Changelog. Always add a release date!

tox.ini
------------------------------------------------------------------------------

Runs tests under multiple Python versions. Can also build docs.

.. code:: ini

    [tox]
    envlist = py37, py38, py39, py310, py311, pypy38
    requires = tox>=4

    [testenv]
    package = wheel
    commands = python -m unittest discover -t . -s tests {posargs}

    [testenv:docs]
    extras = docs
    commands = python -m sphinx -a -d docs/_build/doctrees {posargs} docs docs/_build/html

.. code::

    $ pip install tox

.. code::

    $ tox
    $ tox -e py310

https://tox.wiki/en/stable/

docs
------------------------------------------------------------------------------

Standard, sphinx-quickstart generated docs with the "Read the Docs" theme
enabled.

.. code::

    $ tox -e docs
    $ open docs/_build/html/index.html

https://www.sphinx-doc.org and
https://docs.readthedocs.io/en/stable/

Build and Release
=============================================================================

Use PyPA tools to build distributions and upload them to PyPI:

.. code::

    $ pip install build
    $ pip install twine

.. code::

    $ python -m build
    $ twine upload dist/*

https://pypa-build.readthedocs.io/en/stable/ and
https://twine.readthedocs.io/en/stable/

License
=============================================================================

This package is in the public domain. The included LICENSE file is part of the
example.

