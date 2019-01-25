from io import open
from setuptools import setup, find_packages


def read_file(filename):
    """Return Unicode and universal newlines
    """
    with open(filename, encoding='utf-8') as fp:
        return fp.read()


version = '1.0'

setup(name='mypackage',
      version=version,
      description='My package',
      long_description=read_file('README.rst') + '\n' +
                       read_file('CHANGES.rst'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='my package keywords',
      author='My Name',
      author_email='me@example.com',
      url='https://github.com/me/mypackage',
      license='BSD-2-Clause',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='mypackage.tests',
      install_requires=[
          'setuptools',
      ],
      entry_points={
          'console_scripts': 'myscript=mypackage.mypackage:main',
      },
)
