import argparse
from argparse import Namespace


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(description="Concatenate and clean products.")
    parser.add_argument("directory", type=str, help="Directory containing products.")
    parser.add_argument("output", type=str, help="Output file path.")
    parser.add_argument("-c", "--clean", action="store_true", help="Clean dataset.")
    parser.add_argument(
        "--concatenate",
        action="store_true",
        help="Concatenate dataset before cleaning.",
    )
    return parser.parse_args()
