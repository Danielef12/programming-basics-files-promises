from source.cli import parse_arguments
from source.functions import (clean_dataset, concatenate_files, read_file,
                              save_file)


def main() -> None:
    args = parse_arguments()
    content = read_file(args.directory)
    if args.concatenate:
        content = [concatenate_files(content)]
        print("Concatenated success!")

    if args.clean:
        content_cleaned = clean_dataset(content)
        print("Cleaned dataset success!")
    else:
        content_cleaned = "\n".join(content)

    save_file(args.output, content_cleaned)


if __name__ == "__main__":
    main()
