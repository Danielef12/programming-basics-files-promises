import argparse
from .modules import tail_of_a_file
from typing import NoReturn


def tail() -> NoReturn:
    parser = argparse.ArgumentParser(description="Show the lasts lines of one or more file.")
    parser.add_argument('files', type=str, nargs='+', help='One or more files to read')
    parser.add_argument("-n", "--lines", type=int, default=10, help="Number of lines to show")
    parser.add_argument("-NUM", "--start", type=int, default=0, help="Number of starting line")

    args = parser.parse_args()
    for filename in args.files:
        tail_of_a_file(filename, args.start, args.lines)
