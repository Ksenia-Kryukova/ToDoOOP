from .tasks import Task


class TodoList:

    def __init__(self, my_list: str) -> None:
        self.my_list = my_list

    def todo_list(self) -> list:
        return self.my_list

    def add_task(self, task: Task) -> None:
        self.my_list.append(task)

    def del_task(self, num: int) -> None:
        del self.my_list[num - 1]

    def create_new_list(self) -> list:
        todo_list: list = []
        return todo_list

    def change_task(self, todo_list: list) -> None:
        todo_list[self.num - 1] = self.task

    def change_task(self, task: str) -> None:
        self.task = task
