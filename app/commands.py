from abc import ABC, abstractmethod
from .todo_lists import TodoList
from .tasks import Task
from .loaders import create_loader
from .savers import create_saver
import .constants
import os


class CommandResult:

    def __init__(self, message: str) -> None:
        self._message = message

    def __str__(self) -> str:
        return self._message


class Command(ABC):

    def __init__(self, args) -> None:
        self.args = args

    @abstractmethod
    def execute(self) -> CommandResult:
        pass


class CreateCommand(Command):

    def execute(self) -> CommandResult:
        todo_list = TodoList(self.args.list_name)
        saver = create_saver(self.args.list_name, self.args.format)
        saver.save_list(todo_list)
        return CommandResult(constants.LIST_READY)


class ListCommand(Command):

    def execute(self) -> CommandResult:
        loader = create_loader(self.args.list_name, self.args.format)
        todo_list = TodoList(loader.load_list())
        return CommandResult(todo_list.to_str())


class AddCommand(Command):

    def execute(self) -> CommandResult:
        loader = create_loader(self.args.list_name, self.args.format)
        todo_list = TodoList(loader.load_list())
        todo_list.add_task(Task(self.args.add))
        saver = create_saver(self.args.list_name, self.args.format)
        saver.save_list(todo_list)
        return CommandResult(constants.SAVED)


class DeleteCommand(Command):

    def execute(self) -> CommandResult:
        loader = create_loader(self.args.list_name, self.args.format)
        todo_list = TodoList(loader.load_list())
        todo_list.del_task(self.args.num)
        saver = create_saver(self.arg.list_name, self.args.format)
        saver.save_list(todo_list)
        return CommandResult(constants.TASK_DEL)


class ChangeTaskCommand(Command):

    def execute(self) -> CommandResult:
        loader = create_loader(self.args.list_name, self.args.format)
        todo_list = TodoList(loader.load_list())
        todo_list.change_task(self.args.num, Task(self.args.task))
        saver = create_saver(self.arg.list_name, self.args.format)
        saver.save_list(todo_list)
        return CommandResult(constants.SAVED)


class DeleteListCommand(Command):

    def execute(self) -> CommandResult:
        file_path = os.path.join(os.getcwd(), self.args.delete_list)
        try:
            os.remove(file_path)
            print(f"Файл удален успешно.")
        except FileNotFoundError:
            print(f"Файл не найден.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла: {e}")


def create_command(args) -> Command:
    if args.create_list:
        return CreateCommand(args)
    elif args.list:
        return ListCommand(args)
    elif args.add:
        return AddCommand(args)
    elif args.delete:
        return DeleteCommand(args)
    elif args.change_task:
        return ChangeTaskCommand(args)
    elif args.delete_list:
        return DeleteListCommand(args)
    elif args.all_lists:
        return AllListsCommand(args)
    


'''
    # гет лист нужно удалить и в мейне печатать
    def get_list(self) -> None:
        if len(self.my_list) == 0:
            print(constants.SUCCESSFUL)
        else:
            for num, task in enumerate(self.my_list, 1):
                print(f'{num}. {task}')

    elif args.change_list:
        if args.json:
            loader = JsonLoader(args.change_list)
        else:
            loader = CsvLoader(args.change_list)
        todo_list = TodoList(loader.load())
        except:
    
        elif args.delete:
            try:
            del self.my_list[num - 1]
            print(constants.TASK_DEL)
            if len(self.my_list) == 0:
                print(constants.SUCCESSFUL)
        except IndexError:
            raise WrongTaskNumberException
            todo_list.del_task(args.delete)
    
         elif args.change_task:
            new_task = Task(args.change_task, args.new_task)
            new_task.change_task(todo_list.todo_list())
            save_list = JsonSaver(args.change_list)
            save_list.save_list(todo_list.todo_list())
    
    try:
            todo_list[self.num - 1] = self.task
        except IndexError:
            raise WrongTaskNumberException
    
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
'''