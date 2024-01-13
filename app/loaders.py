import json
import csv
from abc import ABC, abstractmethod


class AbstactLoader(ABC):

    def __init__(self, list_name: str):
        self.list_name = list_name

    @abstractmethod
    def load_list(self):
        pass


class JsonLoader(AbstactLoader):

    def load_list(self):
        with open(self.list_name, 'r', encoding='utf-8') as file:
            todo_list = json.load(file)
        return todo_list


class CsvLoader(AbstactLoader):

    def load_list(self):
        with open(self.list_name, 'r', encoding='utf-8') as file:
            todo_list = list(csv.reader(file))
        return todo_list
