# Description

## Usage


    python todo_list.py -al CSV            # вывести все списки, сохраненные в CSV
    python todo_list.py -al JSON           # вывести все списки, сохраненные в JSON

    python todo_list.py -c <list_name> CSV          # добавить список
    python todo_list.py -dl <list_name> CSV     # удалить список

    python todo_list.py -l <list_name>                                 # вывести все задачи списка <list_name>
    python todo_list.py -chl <list_name> -a "Купить молока"            # добавить задачу
    python todo_list.py -chl <list_name> -d 2                          # удалить задачу по номеру
    python todo_list.py -chl <list_name> -сht 2 -nt "Купить хлеба"     # изменить задачу под номером


Для всех кратких параметров есть полные алиасы:

    -al    --all-lists
    -c     --create
    -dl    --delete_list
    -l     --list
    -a     --add
    -d     --delete
    -chl   --change_list
    -cht   --change_task
    -nt    --new_task
