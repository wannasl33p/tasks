import typing as tp
from collections import Counter
from collections import defaultdict


def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    #counter
    # temp: int = 0
    # for value in Counter(seq).values():
    #     if value > temp:
    #         temp = value
    # return (len(seq)-temp)
    #dict
    # dct: dict = {}
    # for value in seq:
    #     if value in dct.keys():
    #         dct[value] += 1
    #     else:
    #         dct[value] = 1
    # return sum(dct.values()) - max(dct.values(), default=0)
    #defauldict
    # dct = defaultdict(int)
    # for value in seq:
    #     dct[value] += 1
    # return sum(dct.values()) - max(dct.values(), default=0)
