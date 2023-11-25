"""
Given the root of a binary tree, return the sum of values of its deepest
leaves.
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        deepest_level = -1
        deepest_nodes = []

        def dfs(node, level):
            nonlocal deepest_level, deepest_nodes
            if node is None:
                return
            if level > deepest_level:
                deepest_level = level
                deepest_nodes = [node.val]
            elif level == deepest_level:
                deepest_nodes.append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return sum(deepest_nodes)

    def deepest_leaves_sum(self, root: TreeNode):
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if
                         child]
        return sum(node.val for node in pre)
