from app.constants import ERROR_FileNotFound
import json
import csv


class AbstactLoader:

    def __init__(self, list_name: str):
        self.list_name = list_name


class JsonLoader(AbstactLoader):

    def load(self):
        try:
            with open(self.list_name, 'r', encoding='utf-8') as file:
                todo_list = json.load(file)
            return todo_list
        except FileNotFoundError:
            return ERROR_FileNotFound


class CsvLoader(AbstactLoader):

    def load(self):
        try:
            with open(self.list_name, 'r', encoding='utf-8') as file:
                todo_list = list(csv.reader(file))
            return todo_list
        except FileNotFoundError:
            return ERROR_FileNotFound
