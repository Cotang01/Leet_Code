"""
You are given a string s of lowercase English letters and an integer array
shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet,
(wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1
letters of s, x times.

Return the final string after all such shifts to s are applied.
"""


class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        result = []
        shift = 0
        for i in range(len(shifts) - 1, -1, -1):
            result.append(chr((ord(s[i]) - 97 + shift + shifts[i]) % 26 + 97))
            shift += shifts[i]
        return ''.join(result[::-1])
