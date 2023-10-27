from .args_parser import parse
from .todo_lists import TodoList
from .loaders import CsvLoader


def main():
    args = parse()

    loader = CsvLoader()

    to_do_list = loader.load(args.list)

    if args.list:
        # получить список задач из конкретного списка
        print(to_do_list.tasks())

    print(args.filename, args.count, args.verbose)
