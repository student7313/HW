def filter_by_state(list_of_state, state = 'EXECUTED'):
    """
    Отфильтровывает список 'list_of_state' по ключю 'state'.
    По умолчанию state = 'EXECUTED'. Выводит отфильтрованый список.
    """
    list_of_return = []
    for state_dictionary in list_of_state:
        if state_dictionary['state'] ==  state:
            list_of_return.append(state_dictionary)
    return list_of_return


def sort_by_date (list_on_sort, descending  = True):
    """
    Сортирует вводимый список. Параметр 'descending' задает
    порядок сортировки (по возрастанию или убыванию)
    """
    list_on_sort.sort(key = lambda : dictionary['date'], reverse=descending)
    return list_on_sort
