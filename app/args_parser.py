import argparse
from .constants import GREETINGS


def args_parser():
    parser = argparse.ArgumentParser(prog='To-Do List',
                                     description=GREETINGS)

    parser.add_argument('-al', '--all_lists',
                        help='Вывести все списки')
    parser.add_argument('-dl', '--delete_list',
                        help='Удалить список')
    parser.add_argument('-cl', '--create_list',
                        help='Создать новый список с указанным названием')
    parser.add_argument('-j', '--JSON',
                        help='Формат JSON')
    parser.add_argument('-c', '--CSV',
                        help='Формат CSV')
    parser.add_argument('-l', '--list',
                        help='Вывести все задачи указанного списка')
    parser.add_argument('-chl', '--change_list',
                        help='Изменить указанный список')
    parser.add_argument('-a', '--add',
                        help='Добавить новую задачу в список дел')
    parser.add_argument('-d', '--delete', type=int,
                        help='Удалить задачу по указанному номеру')
    parser.add_argument('-cht', '--change_task', type=int,
                        help='Изменить задачу по указанному номеру на новую')
    parser.add_argument('-n', '--new_task',
                        help='Текст измененной задачи')

    return parser.parse_args()
