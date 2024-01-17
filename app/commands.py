from abc import ABC, abstractmethod
from .todo_lists import TodoList
from .tasks import Task
from .loaders import create_loader
from .savers import create_saver
from .constants import LIST_READY, SAVED, TASK_DEL
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
        return CommandResult(LIST_READY)


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
        return CommandResult(SAVED)


class DeleteCommand(Command):

    def execute(self) -> CommandResult:
        loader = create_loader(self.args.list_name, self.args.format)
        todo_list = TodoList(loader.load_list())
        todo_list.del_task(self.args.num)
        saver = create_saver(self.arg.list_name, self.args.format)
        saver.save_list(todo_list)
        return CommandResult(TASK_DEL)


class ChangeTaskCommand(Command):

    def execute(self) -> CommandResult:
        loader = create_loader(self.args.list_name, self.args.format)
        todo_list = TodoList(loader.load_list())
        todo_list.change_task(self.args.num, Task(self.args.task))
        saver = create_saver(self.args.list_name, self.args.format)
        saver.save_list(todo_list)
        return CommandResult(SAVED)


class DeleteListCommand(Command):

    def execute(self) -> CommandResult:
        file_path = os.path.join(os.getcwd(), self.args.delete_list)
        try:
            os.remove(file_path)
            return CommandResult(f"Файл удален успешно.")
        except FileNotFoundError:
            return CommandResult(f"Файл не найден.")
        except Exception as e:
            return CommandResult(f"Произошла ошибка при удалении файла: {e}")


class AllListsCommand(Command):

    def execute(self) -> CommandResult:
        all_files = os.listdir(os.getcwd())
        files = [f for f in all_files if f.endswith(self.args.all_lists.lower())]
        for file in files:
            print(file)
        return CommandResult('ok')


def create_command(args) -> Command:
    if args.all_lists:
        return AllListsCommand(args)
    elif args.create_list:
        return CreateCommand(args)
    elif args.delete_list:
        return DeleteListCommand(args)
    elif args.list:
        return ListCommand(args)
    elif args.add:
        return AddCommand(args)
    elif args.delete:
        return DeleteCommand(args)
    elif args.change_task:
        return ChangeTaskCommand(args)
