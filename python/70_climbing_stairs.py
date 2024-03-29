"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        fibs = [0, 1]
        for _ in range(n - 1):
            res = fibs[-2] + fibs[-1]
            fibs.append(res)
        return fibs[-1] + fibs[-2]
