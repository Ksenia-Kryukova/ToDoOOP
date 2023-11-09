import os
from .args_parser import args_parser
from .todo_lists import TodoList
from .tasks import Task
from .loaders import JsonLoader
from .savers import JsonSaver


def main():
    args = args_parser()

    if args.create:
        saver = JsonSaver(args.create)
        saver.save_list(saver.create_new_list())
    elif args.list:
        loader = JsonLoader(args.list)
        todo_list = TodoList(loader.load())
        todo_list.get_list()
    elif args.change_list:
        loader = JsonLoader(args.change_list)
        todo_list = TodoList(loader.load())
        if args.add:
            todo_list.add_task(args.add)
        elif args.delete:
            todo_list.del_task(args.delete)
        elif args.change_task:
            new_task = Task(args.change_task, args.new_task)
            new_task.change_task(todo_list.todo_list())
        save_list = JsonSaver(args.change_list)
        save_list.save_list(todo_list.todo_list())
    elif args.all_lists:
        all_files = os.listdir(os.getcwd())
        files = [f for f in all_files if f.endswith(args.all_lists.lower())]
        for file in files:
            print(file)
    elif args.delete_list:
        file_path = os.path.join(os.getcwd(), args.delete_list)
        try:
            os.remove(file_path)
            print(f"Файл '{args.delete_list}' удален успешно.")
        except FileNotFoundError:
            print(f"Файл '{args.delete_list}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла: {e}")
