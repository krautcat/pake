import sys

from pake.cli_parser import OptionParser

def parseopts(args):
    parser = OptionParser()


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    cmd, args = parseopts(args)

if __name__="__main__":
    sys.exit(main())