"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        n = len(prices)
        left = 0
        right = 1
        while right < n:
            sell = prices[left]
            buy = prices[right]
            cur_profit = buy - sell
            if cur_profit > max_profit:
                max_profit = cur_profit
            if sell > buy:
                left = right
            right += 1
        return max_profit
