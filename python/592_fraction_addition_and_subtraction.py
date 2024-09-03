"""
Given a string expression representing an expression of fraction addition and
subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an
integer, change it to the format of a fraction that has a denominator 1.
So in this case, 2 should be converted to 2/1.
"""
import re
from typing import List


class Solution(object):
    def fraction_addition(self, expression):
        reg = r"([+-]?\d+)/(\d+)"
        expression = [[int(x), int(y)] for x, y in re.findall(reg, expression)]
        res = expression[0]
        for frac in expression[1:]:
            res = self.add_fraction(res, frac)
        return '/'.join(self.shrink_fraction(res))

    def add_fraction(self, x: List[int], y: List[int]):
        x_den = x[-1]
        y_den = y[-1]
        if x[-1] != y_den:
            x[0] *= y_den
            x[-1] *= y_den
            y[0] *= x_den
            y[-1] *= x_den
        res = [x[0] + y[0], x[-1]]
        print(res)
        return res

    def shrink_fraction(self, f: List[int]) -> List[str]:
        match f[0]:
            case 0:
                return ['0', '1']
            case _:
                com_div = self.find_biggest_com_div(f[0], f[-1])
                return [str(f[0] // com_div), str(f[-1] // com_div)]

    def find_biggest_com_div(self, n1: int, n2: int) -> int:
        biggest_comm_div = 1
        for i in range(1, abs(n1)+1):
            if n1 % i == 0 and n2 % i == 0:
                biggest_comm_div = i
        return biggest_comm_div
