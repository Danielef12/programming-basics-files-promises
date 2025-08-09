import argparse
from argparse import Namespace


def parser_arguments() -> Namespace:

    parser = argparse.ArgumentParser(description="Editor pdf from command line")

    parser.add_argument(
        "operations",
        choices=["extract", "replace", "add", "delete", "merge", "split"],
        help="Operations to perform",
    )

    parser.add_argument("file_input", nargs="?", help="Input file")
    parser.add_argument("file_output", nargs="?", help="Output file")
    parser.add_argument("text1", nargs="?", help="Text to search/delete/add")
    parser.add_argument("text2", nargs="?", help="Replaced text")

    parser.add_argument("--page", type=int, help="Page number")
    parser.add_argument("--x", type=float, help="X coordinate for add text")
    parser.add_argument("--y", type=float, help="Y coordinate for add text")
    parser.add_argument(
        "--intervals", type=str, help="Pages intervals for splitting (es: '1-5, 10-15')"
    )
    parser.add_argument(
        "--font_size", type=int, default=11, help="Font size for adding text"
    )
    parser.add_argument(
        "additional_file_input", nargs="*", help="Additional fil for merge"
    )

    return parser.parse_args()
