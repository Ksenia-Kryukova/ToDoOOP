import os
from app.args_parser import args_parser
from app.todo_lists import TodoList
from app.tasks import Task
from app.loaders import JsonLoader
from app.savers import JsonSaver


def main():
    args = args_parser()

    if args.create:                                               #  РАБОТАЕТ
        save_list = JsonSaver(args.create)
        save_list.save_list(save_list.create_new_list())
    elif args.list:                                              #  РАБОТАЕТ
        loader = JsonLoader(args.list)
        todo_list = TodoList(loader.load())
        todo_list.get_list()
    elif args.change_list:
        loader = JsonLoader(args.change_list)
        todo_list = TodoList(loader.load())
        if args.add:                                              # TypeError: Object of type TodoList is not JSON serializable
            todo_list.add_task(args.add)
        elif args.delete:                                         #  json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
            todo_list.del_task(args.delete)
        elif args.change_task:                                    #  json.decoder.JSONDecodeError: Expecting value: line 1 column 2 (char 1)
            new_task = Task(args.change_task, args.new_task)
            new_task.change_task(todo_list)
        save_list = JsonSaver(args.change_list)
        save_list.save_list(todo_list)
    elif args.all_lists:
        all_files = os.listdir('/home/kryukova/ToDoOOP/')
        files = [f for f in all_files if f.endswith('json') or f.endswith('csv')]
        for file in files:
            print(file)

    # elif args.delete_list:
