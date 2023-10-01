# Description

## Usage


    python todo_list.py -s CSV            # вывести все списки, сохраненные в CSV
    python todo_list.py -s JSON            # вывести все списки, сохраненные в JSON

    python todo_list.py --add-list <list_name> CSV     # добавить список
    python todo_list.py --delete-list <list_name> CSV  # удалить список

    python todo_list.py -l <list_name> CSV            # вывести все задачи списка <list_name>, сохраненные в CSV (для JSON то же самое)
    python todo_list.py -l <list_name> -a "Купить молока" CSV     # добавить задачу
    python todo_list.py -l <list_name> -с "Купить молока" CSV     # пометить задачу выполненной
    python todo_list.py -l <list_name> -d "Купить молока" CSV     # удалить задачу


Для всех кратких параметров есть полные алиасы:

    -s     --all-lists
    -l     --list
    -a     --add
    -c     --complete
    -d     --delete
