from collections.abc import Iterable, Iterator
from typing import Any


def flat_it(sequence: Iterable[Any]) -> Iterator[Any]:
    """
    :param sequence: iterable with arbitrary level of nested iterables
    :return: generator producing flatten sequence
    """
    for item in sequence:
        if isinstance(item, (str, bytes, int)):
            yield item
        else:
            yield from flat_it(item)
