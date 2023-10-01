from .args_parser import parse


def main():
    args = parse()
    print(args.filename, args.count, args.verbose)
