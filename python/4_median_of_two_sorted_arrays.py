"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


def find_median(nums1: list[int], nums2: list[int]) -> float:
    nums3 = nums1 + nums2
    n = len(nums3)
    if n % 2 != 0:
        return nums3[n//2]
    else:
        return (nums3[n//2] + nums3[n//2 - 1]) / 2
