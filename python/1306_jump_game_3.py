"""
Given an array of non-negative integers arr, you are initially positioned at
start index of the array. When you are at index i, you can jump to i + arr[i]
or i - arr[i], check if you can reach any index with value 0.
"""


class Solution:
    # iterative
    def can_reach(self, arr: list[int], start: int) -> bool:
        stack = [start]
        seen = set()
        seen.add(start)
        while stack:
            position = stack.pop()
            if arr[position] == 0:
                return True
            left = position - arr[position]
            right = position + arr[position]
            if 0 <= left < len(arr) and left not in seen:
                seen.add(left)
                stack.append(left)
            if 0 <= right < len(arr) and right not in seen:
                seen.add(right)
                stack.append(right)
        return False

    # bfs
    def can_reach_2(self, arr: list[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or \
                self.can_reach_2(arr, start + arr[start]) or \
                self.can_reach_2(arr, start - arr[start])
        return False
