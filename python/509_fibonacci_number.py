"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding
ones, starting from 0 and 1.
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def fib_2(self, n: int) -> int:
        match n:
            case 0:
                return 0
            case 1:
                return 1
        cache = [0 for _ in range(n + 1)]
        cache[0] = 0
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]
