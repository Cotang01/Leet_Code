"""
Given an integer n, return any array containing n unique integers such that
they add up to 0.
"""


class Solution:
    def sum_zero(self, n: int) -> list[int]:
        res = []
        for i in range(1, n, 2):
            res.append(-i)
            res.append(i)
        if not n % 2 == 0:
            res.append(0)
        return res
