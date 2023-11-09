from .constants import NO_NUMBER


class Task:

    def __init__(self, num: int, task: str) -> None:
        self.num = num
        self.task = task

    def change_task(self, todo_list: list) -> None:
        try:
            todo_list[self.num - 1] = self.task
        except IndexError:
            print(NO_NUMBER)
