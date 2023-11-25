"""
Given two binary search trees root1 and root2, return a list containing all
the integers from both trees sorted in ascending order.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n + m); Space: O(n + m) both
class Solution:
    def get_all_elements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        return sorted(self._traverse_and_gather(root1, []) +
                      self._traverse_and_gather(root2, []))

    def _traverse_and_gather(self, node: TreeNode, gathered):
        if node:
            gathered.append(node.val)
            self._traverse_and_gather(node.left, gathered)
            self._traverse_and_gather(node.right, gathered)
        return gathered

    def get_all_elements_2(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        stack1, stack2 = [], []
        result = []

        while stack1 or stack2 or root1 or root2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                node = stack1.pop()
                result.append(node.val)
                root1 = node.right
            else:
                node = stack2.pop()
                result.append(node.val)
                root2 = node.right
        return result
