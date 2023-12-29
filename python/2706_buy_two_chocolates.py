"""
You are given an integer array prices representing the prices of various
chocolates in a store. You are also given a single integer money, which
represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some
non-negative leftover money. You would like to minimize the sum of the prices
of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two
chocolates. If there is no way for you to buy two chocolates without ending
up in debt, return money. Note that the leftover must be non-negative.
"""
from itertools import combinations


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        max_leftover = float('-inf')
        for comb in [*combinations(prices, 2)]:
            leftover = money - (comb[0] + comb[1])
            if max_leftover < leftover:
                max_leftover = leftover
        if max_leftover >= 0:
            return max_leftover
        return money

    def buyChoco2(self, prices: list[int], money: int) -> int:
        max_leftover = float('-inf')
        for i in range(len(prices) - 1):
            for j in range(1 + i, len(prices)):
                leftover = money - (prices[i] + prices[j])
                if max_leftover < leftover:
                    max_leftover = leftover
        if max_leftover >= 0:
            return max_leftover
        return money

    def buyChoco3(self, prices: list[int], money: int) -> int:
        x = sum(sorted(prices)[:2])
        return money * (money < x) + (money - x) * (money >= x)

    def buyChoco4(self, prices: list[int], money: int) -> int:
        min1 = 101
        min2 = 101
        for i in prices:
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        x = min1 + min2
        return money * (money < x) + (money - x) * (money >= x)
