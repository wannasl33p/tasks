import typing as tp
import heapq

def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    value = []
    for numbers in seq :
        for num in numbers :
            heapq.heappush(value, num)
    
    return heapq.nsmallest(len(value),value)

    
print(merge([[1,23,3],[123,312,124]]))