"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a
type of stone you have. You want to know how many of the stones you have are
also jewels.

Letters are case sensitive, so "a" is considered a different type of stone
from "A".
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for i in stones:
            if i in jewels:
                counter += 1
        return counter

    def numJewelsInStones_2(self, jewels: str, stones: str) -> int:
        return sum([stones.count(j) for j in jewels])
