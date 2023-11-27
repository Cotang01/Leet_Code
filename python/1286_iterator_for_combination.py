"""
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the
object with a string characters of sorted distinct lowercase English letters
and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in
lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
"""

from itertools import combinations


class CombinationIterator2:

    def __init__(self, characters: str, combination_length: int):
        self.characters: str = characters
        self.combination_length: int = combination_length
        self.char_combs = [''.join(comb) for comb in combinations(
            self.characters, self.combination_length)]
        self.index = -1

    def next(self) -> str:
        self.index += 1
        return self.char_combs[self.index]

    def hasNext(self) -> bool:
        if self.index == len(self.char_combs) - 1:
            return False
        return True
