"""
Given a string s, return the number of unique palindromes of length three
that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence,
it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        result = 0
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            for k in range(i + 1, j):
                between.add(s[k])
            result += len(between)
        return result
