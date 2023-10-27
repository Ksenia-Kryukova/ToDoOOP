from .tasks import Task


class TodoList:
    def __init__(self, list_name) -> None:
        self.name = list_name
        self._tasks: list = []

    def add_task(self, task: Task):
        self._tasks.append(task)

    def tasks(self):
        return self._tasks
