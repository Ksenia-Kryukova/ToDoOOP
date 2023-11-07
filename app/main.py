# import os
from app.args_parser import args_parser
from app.todo_lists import TodoList
from app.tasks import Task
from app.loaders import JsonLoader
from app.savers import JsonSaver


def main():
    args = args_parser()

    if args.create:
        save_list = JsonSaver(args.create)
        save_list.save_list(save_list.create_new_list())
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
            new_task.change_task(todo_list)
        save_list = JsonSaver(args.change_list)
        save_list.save_list(todo_list)
    # elif args.all_lists:

    # elif args.delete_list:
