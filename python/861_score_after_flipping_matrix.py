"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that
row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the
matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including
zero moves).
"""
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        def _flip_spot(grid_, i_, j_):
            if grid_[i_][j_] == 0:
                grid_[i_][j_] = 1
            else:
                grid_[i_][j_] = 0

        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    _flip_spot(grid, i, j)

        for j in range(n):
            col = []
            for i in range(m):
                col.append(grid[i][j])
            if col.count(0) * 2 > len(col):
                for k in range(m):
                    _flip_spot(grid, k, j)

        for i in range(m):
            bin_number = []
            for j in range(n):
                bin_number.append(str(grid[i][j]))
            res += int(''.join(bin_number), 2)

        return res
