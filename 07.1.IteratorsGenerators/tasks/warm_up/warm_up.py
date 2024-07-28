from collections.abc import Generator
from typing import Any


def transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    """
    :param matrix: rectangular matrix
    :return: transposed matrix
    """
    return [list(item) for item in list(zip(*matrix))]


def uniq(sequence: list[Any]) -> Generator[Any, None, None]:
    """
    :param sequence: arbitrary sequence of comparable elements
    :return: generator of elements of `sequence` in
    the same order without duplicates
    """
    for i, item in enumerate(iter(sequence)):
        if item not in sequence[:i]:
            yield item


def dict_merge(*dicts: dict[Any, Any]) -> dict[Any, Any]:
    """
    :param *dicts: flat dictionaries to be merged
    :return: merged dictionary
    """
    merged_dict: dict[Any, Any] = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict


def product(lhs: list[int], rhs: list[int]) -> int:
    """
    :param rhs: first factor
    :param lhs: second factor
    :return: scalar product
    """
    return sum([lft * rgt for lft, rgt in zip(lhs, rhs)])


matr = [[1, 2], [3, 4], [5, 6]]
print(transpose(matrix=matr))
