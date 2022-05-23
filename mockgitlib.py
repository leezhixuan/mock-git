import argparse
import sys


from init_command import init

parser = argparse.ArgumentParser(description="Mock Git")
subparsers = parser.add_subparsers(title="Commands", dest="command")
subparsers.required = True # all invocations of mgit requires a command that follows, much like Git

# init command
argsp = subparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="The file path of the location to create the repository.")

def main(argsv=sys.argv[1:]):
    args = parser.parse_args(argsv)

    if args.command == "init" : init(args)

