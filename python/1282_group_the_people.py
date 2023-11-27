"""
There are n people that are split into some unknown number of groups.
Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of
the group that person i is in. For example, if groupSizes[1] = 3, then
person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size
groupSizes[i].

Each person should appear in exactly one group, and every person must be in a
group. If there are multiple answers, return any of them. It is guaranteed
that there will be at least one valid solution for the given input.
"""
from collections import defaultdict


class Solution:

    def group_the_people(self, group_sizes: list[int]) -> list[list[int]]:
        groups = {}
        res = []
        for i in range(len(group_sizes)):
            groups[group_sizes[i]] = groups.get(group_sizes[i], [])
            groups[group_sizes[i]].append(i)
        for k, v in groups.items():
            step = k
            for i in range(len(v) // k):
                res.append(v[step - k:step])
                step += k
        return res

    def group_the_people_2(self, group_sizes: list[int]) -> list[list[int]]:
        groups = defaultdict(list)
        res = []
        for i, size in enumerate(group_sizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
        return res
