from .tasks import Task
from .constants import WrongTaskNumberException


class TodoList:

    def __init__(self, list_name: str) -> None:
        self.list_name = list_name
        self._my_list: list = []

    def to_str(self) -> str:    # вернуть строку
        return self._my_list

    def add_task(self, task: Task) -> None:
        self._my_list.append(task)

    def del_task(self, num: int) -> None:
        try:
            del self._my_list[num - 1]
        except IndexError:
            raise WrongTaskNumberException

    def change_task(self, num: int, task: Task) -> None:
        try:
            self._my_list[num - 1] = task
        except IndexError:
            raise WrongTaskNumberException
