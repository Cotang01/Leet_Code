"""
Given an integer array nums, find three numbers whose product is maximum and
return the maximum product.
"""


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximum_product_2(self, nums: list[int]) -> int:
        max1 = -1001
        max2 = -1001
        max3 = -1001
        min1 = 1001
        min2 = 1001
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, min1 * min2 * max1)
