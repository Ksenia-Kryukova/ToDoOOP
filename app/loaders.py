import json
import csv
from abc import ABC, abstractmethod
from .constants import CannotSaveTodoList, ERROR_FileNotFound


class AbstactLoader(ABC):

    def __init__(self, list_name: str) -> None:
        self.list_name = list_name

    @abstractmethod
    def load_list(self):
        pass


class JsonLoader(AbstactLoader):

    def load_list(self) -> list:
        try:
            with open(self.list_name, 'r', encoding='utf-8') as file:
                todo_list = json.load(file)
            return todo_list
        except FileNotFoundError:
            raise CannotSaveTodoList(ERROR_FileNotFound)


class CsvLoader(AbstactLoader):

    def load_list(self) -> list:
        try:
            with open(self.list_name, 'r', encoding='utf-8') as file:
                todo_list = list(csv.reader(file))
            return todo_list
        except FileNotFoundError:
            raise CannotSaveTodoList(ERROR_FileNotFound)


def create_loader(list_name: str, format: str):
    if format == 'json':
        return JsonLoader(list_name)
    elif format == 'csv':
        return CsvLoader(list_name)
