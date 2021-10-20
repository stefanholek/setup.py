from setuptools import setup, find_packages

version = '1.0'

setup(name='mypackage',
      version=version,
      description='My package',
      long_description=open('README.rst').read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='my package keywords',
      author='My Name',
      author_email='me@example.com',
      url='https://github.com/me/mypackage',
      project_urls={
          'Documentation': 'https://mypackage.readthedocs.io/en/stable',
          'Issue Tracker': 'https://github.com/me/mypackage/issues',
          'Source Code': 'https://github.com/me/mypackage',
      },
      license='BSD-2-Clause',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points={
          'console_scripts': 'myscript=mypackage.mypackage:main',
      },
)
