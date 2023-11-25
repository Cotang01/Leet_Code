"""
The letter value of a letter is its position in the alphabet starting from 0
(i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the
concatenation of the letter values of each letter in s, which is then
converted into an integer.
"""


class Solution:
    def is_sum_equal(self, first: str, second: str, target: str) -> bool:
        first_value = int(''.join([str(ord(i) - ord('a')) for i in first]))
        second_value = int(''.join([str(ord(i) - ord('a')) for i in second]))
        target_value = int(''.join([str(ord(i) - ord('a')) for i in target]))
        return first_value + second_value == target_value

    def is_sum_equal_2(self, first: str, second: str, target: str)\
            -> bool:
        table = str.maketrans('abcdefghij', '0123456789')
        return int(first.translate(table)) + \
               int(second.translate(table)) == \
               int(target.translate(table))
