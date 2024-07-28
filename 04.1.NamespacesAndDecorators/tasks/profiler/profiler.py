from datetime import datetime


def profiler(func):  # type: ignore
    """
    Returns profiling decorator, which counts calls of function
    and measure last function execution time.
    Results are stored as function attributes: `calls`, `last_time_taken`
    :param func: function to decorate
    :return: decorator, which wraps any function passed
    """
    func.last_time_taken = 0
    func.calls = 0

    def wrapper(*args, **kwargs):
        time_1: datetime = datetime.now()
        result = func(*args, **kwargs)
        time_2: datetime = datetime.now()
        func.calls += 1
        func.last_time_taken = time_2 - time_1
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__
    return wrapper
