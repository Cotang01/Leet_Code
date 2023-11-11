"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.makeBST(nums, 0, len(nums))

    def makeBST(self, nums: list[int], start: int, end: int):
        if start >= end:
            return None
        return TreeNode(
            val=nums[(start + end) // 2],
            left=self.makeBST(nums, start, (start + end) // 2),
            right=self.makeBST(nums, 1 + ((start + end) // 2), end)
        )
