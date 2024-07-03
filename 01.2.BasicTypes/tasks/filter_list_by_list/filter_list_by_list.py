def filter_list_by_list(lst_a: list[int] | range, lst_b: list[int] | range) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    f_lst = []
    
    for num in lst_a :
        if num in f_lst :
            f_lst.append(num)
            continue
        if num not in lst_b :
            f_lst.append(num)
    return f_lst    