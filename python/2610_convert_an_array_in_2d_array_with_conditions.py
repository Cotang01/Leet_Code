"""
You are given an integer array nums. You need to create a 2D array from nums
satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_d = {}
        max_rows = 0
        for n in nums:
            nums_d[n] = nums_d.get(n, 0) + 1
            max_rows = max(max_rows, nums_d[n])
        for i in range(max_rows):
            buf = []
            for k, v in nums_d.items():
                if v - 1 > -1:
                    buf.append(k)
                    nums_d[k] -= 1
            res.append(buf)
        return res

    def findMatrix2(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        res = []

        for n in nums:
            if freq[n] >= len(res):
                res.append([])
            res[freq[n]].append(n)
            freq[n] += 1

        return res
