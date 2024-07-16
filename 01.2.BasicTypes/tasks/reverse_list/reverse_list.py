def reverse_iterative(lst: list[int]) -> list[int]:
    """
    Return reversed list. You can use only iteration
    :param lst: input list
    :return: reversed list
    """
    new: list[int] = []
    j: int = len(lst) - 1
    while j >= 0:
        new.append(lst[j])
        j -= 1
    return new


def reverse_inplace_iterative(lst: list[int]) -> None:
    """
    Revert list inplace. You can use only iteration
    :param lst: input list
    :return: None
    """
    j: int = len(lst) - 1
    for i in range(len(lst)//2):
        lst[i], lst[j] = lst[j], lst[i]
        j -= 1


def reverse_inplace(lst: list[int]) -> None:
    """
    Revert list inplace with reverse method
    :param lst: input list
    :return: None
    """
    lst = lst.reverse()


def reverse_reversed(lst: list[int]) -> list[int]:
    """
    Revert list with `reversed`
    :param lst: input list
    :return: reversed list
    """
    listy: list[int] = list(reversed(lst))
    return listy


def reverse_slice(lst: list[int]) -> list[int]:
    """
    Revert list with slicing
    :param lst: input list
    :return: reversed list
    """
    listy: list[int] = lst[::-1]
    return listy
