"""
You are given a string s and array queries where queries[i] = [lefti, righti, ki].
We may rearrange the substring s[lefti...righti] for each query and then
choose up to ki of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations
above, the result of the query is true. Otherwise, the result is false.

Return a boolean array answer where answer[i] is the result of the ith query
queries[i].
"""
from typing import List
from collections import Counter, deque


class Solution:
    def canMakePaliQueriesMatrix(self, s: str, queries: List[List[int]]) -> List[bool]:
        letters_n = 26
        ord_a = 97
        dp = [[0] * letters_n]
        for i in range(len(s)):
            new = dp[i][:]
            j = ord(s[i]) - ord_a
            new[j] += 1
            dp.append(new)
        return [sum(dp[r+1][i] - dp[l][i] % 2 for i in range(letters_n)) // 2 <= k
                for l, r, k in queries]

    def FAILED_canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        s_char_counts = Counter(s)
        new_s = deque()
        append_dir = 1
        for k, v in sorted(s_char_counts.items(), key=lambda x: x[1]):
            vb = v
            if vb % 2 == 0:
                while vb >= 2:
                    new_s.appendleft(k)
                    new_s.append(k)
                    vb -= 2
            else:
                if append_dir > 0:
                    new_s.append(k)
                    append_dir *= -1
                else:
                    new_s.appendleft(k)
                    append_dir *= -1
        s = ''.join(new_s)

        def is_palin(s_: str, shifts: int) -> bool:
            n = len(s_)
            l = 0
            r = n - 1
            while l < r:
                if s_[l] != s_[r]:
                    if shifts:
                        pivot = n // 2
                        odd_len = n % 2
                        l = pivot - 1
                        r = pivot + odd_len
                        s_ = [*s_]
                        border = len(s_)
                        while shifts and r < border:
                            wanted_char = s_[l]
                            if wanted_char in s_char_counts:
                                s_[r] = wanted_char
                            l -= 1
                            r += 1
                            shifts -= 1
                        return is_palin(''.join(s_), 0)
                    return False
                l += 1
                r -= 1
            return True

        return [is_palin(s[start:stop + 1], shifts)
                for start, stop, shifts in queries]


