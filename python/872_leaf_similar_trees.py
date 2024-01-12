"""
Consider all the leaves of a binary tree, from left to right order, the values
of those leaves form a leaf value sequence.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))

    def leafSimilar_2(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self._get_leafs(root1, []) == self._get_leafs(root2, [])

    def _get_leafs(self, node, gathered) -> list[int]:
        if node:
            if not node.left and not node.right:
                gathered.append(node.val)
        if node.left:
            self._get_leafs(node.left, gathered)
        if node.right:
            self._get_leafs(node.right, gathered)
        return gathered
