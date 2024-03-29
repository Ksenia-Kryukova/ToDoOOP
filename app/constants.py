GREETINGS = '''Добро пожаловать в To-Do List!
    Используйте комманды для работы со списками.
    Все доступные комманды можно увидеть по команде --help или -h'''
COMMANDS = 'Вам доступны перечисленные ниже команды'
LIST_READY = 'Список создан'
ERROR_FileNotFound = '''У вас еще нет списка дел с таким названием.
    Попробуйте открыть другой или создать новый'''
SAVED = 'Изменения сохранены. До встречи!'
INPUT_TASK = 'Введите задачу: '
Q_CONTINUE_INPUT = 'Продолжить ввод задач? да|нет'
TASK_DEL = 'Задача успешно удалена из списка'
SUCCESSFUL = 'Молодец! Ты выполнил все задачи)'
NO_NUMBER = 'Такого номера нет в списке, выберите другой'


class ToDoListBaseException(Exception):
    pass


class WrongTaskNumberException(ToDoListBaseException):
    pass


class CannotSaveTodoList(ToDoListBaseException):
    pass
