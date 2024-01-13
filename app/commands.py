from abc import ABC, abstractmethod
from .todo_lists import TodoList
import os
from .tasks import Task
from .loaders import JsonLoader, CsvLoader
from .savers import JsonSaver, CsvSaver


class CommandResult:

    def __init__(self, message: str) -> None:
        self._message = message

    def message(self) -> str:
        return self._message

    def __str__(self) -> str:
        return self._message


class Command(ABC):  # абстрактный класс команды

    def __init__(self, args) -> None:
        self.args = args

    @abstractmethod
    def execute(self) -> CommandResult:
        pass


class CreateCommand(Command):    # класс конкретной команды

    def execute(self) -> CommandResult:
        saver = create_saver(self.args, self.args.format)
        todo_list = TodoList(self.args.list_name)
        saver.save_list(todo_list)
        return CommandResult(LIST_READY)


class ListCommand(Command):

    def execute(self) -> CommandResult:
        loader = create_loader(args.list, self.args.format)
        todo_list = TodoList(loader.load())
        return todo_list.get_list()


# чтобы добавить новую команду, нужно создать класс с методом def execute(self) -> CommandResult и добавить его вызов в create_command
def create_command(args) -> Command:
    if args.create:
        return CreateCommand(args)
    elif args.list:
        return ListCommand(args)
    # и т.д. Здесь у нас всё же останется портянка if-ов, от них нам никуда не деться. Но она будет 1) изолирована в одной функции 2) очень простая, т.к. будет просто возвращать объект нужного класса


'''
 if args.create_list:
        if args.json:
            saver = JsonSaver(args.create_list)
        else:
            saver = CsvSaver(args.create_list)
        saver.save_list(saver.create_new_list())
    
    while True:
            task = input(constants.INPUT_TASK)
            todo_list.append(task)
            print(constants.Q_CONTINUE_INPUT)
            if input().lower() == 'нет':
                print(constants.LIST_READY)
                break

    elif args.list:
    
    
    try:
            with open(self.list_name, 'r', encoding='utf-8') as file:
                todo_list = json.load(file)
            return todo_list
        except FileNotFoundError:
            return ERROR_FileNotFound

        if args.json:
            loader = JsonLoader(args.list)
        else:
            loader = CsvLoader(args.list)
        todo_list = TodoList(loader.load())
        todo_list.get_list()
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
        if args.add:
            todo_list.add_task(args.add)
    
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