"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        for _ in range(n - 2):
            t.append(t[-3] + t[-2] + t[-1])
        return t[n]

    def tribonacci_2(self, n: int) -> int:
        match n:
            case 0:
                return 0
            case 1:
                return 1
        cache = [0 for _ in range(n + 1)]
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
        return cache[n]

