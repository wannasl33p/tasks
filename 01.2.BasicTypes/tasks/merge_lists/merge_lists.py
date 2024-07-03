def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    sorted_lst = []
    i, j = 0, 0
    while i < len(lst_a) and j < len(lst_b):
        sorted_lst.append(lst_a[i] if lst_a[i] < lst_b[j] else lst_b[j])
        if lst_a[i] < lst_b[j]:
            i += 1
        else:
            j += 1

    sorted_lst.extend(lst_a[i:])
    sorted_lst.extend(lst_b[j:])

    return sorted_lst

def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    return (sorted(lst_a+lst_b))