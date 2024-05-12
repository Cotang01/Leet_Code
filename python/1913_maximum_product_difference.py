"""
The product difference between two pairs (a, b) and (c, d) is defined as
(a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) -
(2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such
that the product difference between pairs (nums[w], nums[x]) and (nums[y],
nums[z]) is maximized.

Return the maximum such product difference.
"""
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]

    def maxProductDifference2(self, nums: List[int]) -> int:
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')
        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        return max1 * max2 - min1 * min2
