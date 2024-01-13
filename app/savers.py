import json
import csv
from abc import ABC, abstractmethod


class AbstactSaver(ABC):

    def __init__(self, list_name: str):
        self.list_name = list_name

    @abstractmethod
    def save_list(self, todo_list: list):
        pass


class JsonSaver(AbstactSaver):

    def save_list(self, todo_list: list) -> None:
        with open(self.list_name, 'w', encoding='utf-8') as file:
            json.dump(todo_list, file)


class CsvSaver(AbstactSaver):

    def save_list(self, todo_list: list) -> None:
        with open(self.list_name, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            columns = ['num', 'task']
            writer.writerow(columns)
            writer.writerows(todo_list)
