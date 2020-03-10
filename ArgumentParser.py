import getopt
import sys


class ArgumentParser:
    def __init__(self, argv, usage):
        self.argv = argv
        self.usage = usage

    def validate(self):
        is_valid = True

        if len(self.argv) <= 0:
            is_valid = False

        return is_valid

    def print_usage(self):
        print(self.usage)

    def parse(self, short_opt, long_opt):
        if not self.validate():
            return []

        try:
            opts, _ = getopt.getopt(self.argv, ":".join(short_opt) + ":", long_opt)
        except getopt.GetoptError:
            self.print_usage()
            sys.exit(2)

        args = []
        for opt, arg in opts:
            if opt in short_opt or long_opt:
                args.append([opt, arg])

        return args

    @staticmethod
    def get_value_by_key(key, args):
        for i in args:
            k, v = i
            if k == key:
                return v

        return ''