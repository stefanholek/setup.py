import sys

from .mypackage import main


if __name__ == '__main__':
    sys.argv[0] = 'python -m mypackage'
    sys.exit(main())
