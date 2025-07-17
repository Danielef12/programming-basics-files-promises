import argparse
from .modules import head_of_a_file


def head():
    parser = argparse.ArgumentParser(description="Show the first lines of one or more files.")
    parser.add_argument("files", nargs="+", help="Paths of the files to read")
    parser.add_argument("-n", "--lines", type=int, default=10, help="Number of lines to show (default=10)")
    parser.add_argument("-v", "--name", action="store_true", help="Show filename before content")

    args = parser.parse_args()

    for file_path in args.files:
        head_of_a_file(file_path, args.lines, args.name)

