from .todo_lists import TodoList


class AbstactLoader:
    pass


class JsonLoader(AbstactLoader):
    pass


class CsvLoader(AbstactLoader):
    def load(self, list_name):
        # загрузка из файла
        pass

        # создаём экземпляр списка
        to_do_list = TodoList(list_name)
        return to_do_list
