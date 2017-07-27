import argparse


class OptionParser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__command = ""
        subparsers = self.__parser.add_subparsers()

        # create the parser for the "a" command
        parser_install = subparsers.add_parser('install', dest=self.__command)
        # parser_install.add_argument('bar', type=int, help='bar help')

        # create the parser for the "b" command
        parser_build = subparsers.add_parser('build', dest=self.__command)
        parser_build.add_argument('--source', action='store_true')
        parser_build.add_argument('--bin-wheel', action='store_true')

        # create the parser for the "b" command
        parser_clean = subparsers.add_parser('clean', dest=self.__command)
        parser_clean.add_argument('--all', action='store_true')

        # create the parser for the "b" command
        parser_upload = subparsers.add_parser('upload')
        parser_upload.add_argument('--test', type='store_true', dest=self.__command)

    def parse(self, args):
        return self.__parser.parse_args(args)