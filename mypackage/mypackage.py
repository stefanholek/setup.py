import argparse

import pkg_resources
__version__ = pkg_resources.get_distribution('mypackage').version


def main():
    parser = argparse.ArgumentParser(description='My package')
    parser.add_argument('-v', '--version',
                        help='show the version string and exit',
                        action='store_true')

    args = parser.parse_args()
    if args.version:
        print('mycli %s' % __version__)
    else:
        parser.print_usage()
