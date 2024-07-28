from collections.abc import Callable
from typing import Any, TypeVar
from collections import OrderedDict


Function = TypeVar("Function", bound=Callable[..., Any])


def cache(max_size: int) -> Callable[[Function], Function]:
    """
    Returns decorator, which stores result of function
    for `max_size` most recent function arguments.
    :param max_size: max amount of unique arguments to store values for
    :return: decorator, which wraps any function passed
    """

    def cache(func: Callable):
        dct = OrderedDict()

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in dct:
                dct.move_to_end(key=key)
                return dct[key]
            result = func(*args, **kwargs)
            dct[key] = result
            dct.move_to_end(key=key)
            if len(dct) > max_size:
                dct.popitem(last=False)
            return result

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        wrapper.__annotations__ = func.__annotations__
        return wrapper

    return cache
