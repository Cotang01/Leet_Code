"""
Given an integer array nums, find a subarray that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max_n = min_n = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            candidates = (cur, max_n * cur, min_n * cur)
            max_n = max(candidates)
            min_n = min(candidates)
            res = max(res, max_n)
        return res

