"""
You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness
value happiness[i]. You want to select k children from these n children in k
turns.

In each turn, when you select a child, the happiness value of all the children
that have not been selected till now decreases by 1. Note that the happiness
value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you
can achieve by selecting k children.
"""
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        i = -1
        decrement = 0
        for _ in range(k):
            cur_max = happiness[i] - decrement
            res += cur_max if cur_max > 0 else 0
            i -= 1
            decrement += 1
        return res
