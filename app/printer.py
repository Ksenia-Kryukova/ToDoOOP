from .constants import ToDoListBaseException
from .commands import CommandResult


class SuccessPrinter:
    def __init__(self, result: CommandResult):
        self.result = result

    def print(self):
        print(self.result)


class ErrorPrinter:
    def __init__(self, exception: ToDoListBaseException):
        self.exception = exception

    def print(self):
        print(self.exception)
