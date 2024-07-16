from collections.abc import Sequence


def find_median(nums1: Sequence[int], nums2: Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    sorted_nums = sorted(nums1+nums2)
    return float(sorted_nums[len(sorted_nums)//2]) if len(sorted_nums) % 2 != 0 else (sorted_nums[len(sorted_nums)//2]
                                                                                      + sorted_nums[len(sorted_nums) //
                                                                                                    2 - 1]) / 2
