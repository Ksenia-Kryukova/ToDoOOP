from app.tasks import Task
from app import constants


class TodoList:

    def __init__(self, my_list: list) -> None:
        self.my_list = my_list

    def todo_list(self) -> list:
        return self.my_list

    def add_task(self, task: Task) -> None:
        self.my_list.append(task)

    def del_task(self, num: int) -> None:
        try:
            del self.my_list[num - 1]
            print(constants.TASK_DEL)
            if len(self.my_list) == 0:
                print(constants.SUCCESSFUL)
        except IndexError:
            print(constants.NO_NUMBER)

    def get_list(self):
        if len(self.my_list) == 0:
            print(constants.SUCCESSFUL)
        else:
            for num, task in enumerate(self.my_list, 1):
                print(f'{num}. {task}')
