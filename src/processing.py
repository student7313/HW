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