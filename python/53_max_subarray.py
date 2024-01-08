"""
Given an integer array nums, find the subarray with the largest sum, and
return its sum.
"""


class Solution:
    def max_sub_array(self, nums: list[int]) -> int:
        max_so_far = -10_001
        max_ending_here = 0
        for i in range(len(nums)):
            max_ending_here += nums[i]
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

    def max_sub_array_2p(self, nums: list[int]) -> int:
        left = 0
        right = 0
        max_so_far = -10_001
        max_ending_here = 0
        n = len(nums)
        while right < n:
            max_ending_here += nums[right]
            max_so_far = max(max_so_far, max_ending_here)
            while max_ending_here < 0:
                max_ending_here -= nums[left]
                left += 1
            right += 1
        return max_so_far
