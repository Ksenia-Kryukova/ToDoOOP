import json
import csv
from abc import ABC, abstractmethod
from .constants import CannotSaveTodoList, ERROR_FileNotFound


class AbstactSaver(ABC):

    def __init__(self, list_name: str) -> None:
        self.list_name = list_name

    @abstractmethod
    def save_list(self, todo_list: list):
        pass


class JsonSaver(AbstactSaver):

    def save_list(self, todo_list: list) -> None:
        try:
            with open(self.list_name, 'w', encoding='utf-8') as file:
                json.dump(todo_list, file)
        except FileNotFoundError:
            raise CannotSaveTodoList(ERROR_FileNotFound)


class CsvSaver(AbstactSaver):

    def save_list(self, todo_list: list) -> None:
        try:
            with open(self.list_name, 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                columns = ['num', 'task']
                writer.writerow(columns)
                writer.writerows(todo_list)
        except FileNotFoundError:
            raise CannotSaveTodoList(ERROR_FileNotFound)


def create_saver(list_name: str, format: str):
    if format == 'json':
        return JsonSaver(list_name)
    elif format == 'csv':
        return CsvSaver(list_name)
