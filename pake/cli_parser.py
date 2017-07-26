import argparse



class OptionParser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        subparsers = self.__parser.add_subparsers()

        # create the parser for the "a" command
        parser_install = subparsers.add_parser('install', help='install help')
        parser_install.add_argument('bar', type=int, help='bar help')

        # create the parser for the "b" command
        parser_build = subparsers.add_parser('b', help='b help')
        parser_build.add_argument('--source', type='store_true', default )