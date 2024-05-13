"""
You are given two strings s and t such that every character occurs at most once
in s and t is a permutation of s.

The permutation difference between s and t is defined as the sum of the
absolute difference between the index of the occurrence of each character in s
and the index of the occurrence of the same character in t.

Return the permutation difference between s and t.
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        for i in range(len(s)):
            res += abs(i - t.index(s[i]))
        return res

    def findPermutationDifference2(self, s: str, t: str) -> int:
        res = 0
        n = len(s)
        s_dict = {s[i]: i for i in range(n)}
        for i in range(n):
            res += abs(i - s_dict[t[i]])
        return res

