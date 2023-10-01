from .tasks import Task


class TodoList:
    def __init__(self, list_name) -> None:
        self.name = list_name
        self.tasks: list = []
    
    def add_task(self, task: Task):
        self.tasks.append(task)
