import typing as tp
from collections import Counter

def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    temp = 0
    for value in Counter(seq).values():
        if value>temp :
            temp=value
    return(len(seq)-temp)


print(get_min_to_drop([1, 2, 3, 1, 1,7,8,9])) 