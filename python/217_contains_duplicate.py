"""
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:  # O(n) O(n)
        return len(set(nums)) != len(nums)

    def containsDuplicate2(self, nums: list[int]) -> bool:  # O(n log(n)) O(1)
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
