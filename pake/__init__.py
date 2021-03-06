import sys

from pake.cli_parser import OptionParser

def parseopts(args):
    parser = OptionParser()
    return parser.parse(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    returns = parseopts(args)

    print(returns)

if __name__=="__main__":
    sys.exit(main())