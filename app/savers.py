import json
import csv
from app import constants


class AbstactSaver:

    def __init__(self, list_name: str):
        self.list_name = list_name

    def create_new_list(self) -> list:
        todo_list = []
        while True:
            task = input(constants.INPUT_TASK)
            todo_list.append(task)
            print(constants.Q_CONTINUE_INPUT)
            if input().lower() == 'нет':
                print(constants.LIST_READY)
                break
        return todo_list


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
