"""
You are given a sorted integer array arr containing 1 and prime numbers, where
all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction
arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of
integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
"""
from typing import List
from itertools import combinations


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        return [*sorted([*combinations(arr, 2)], key=lambda x: x[0]/x[1])[k-1]]
