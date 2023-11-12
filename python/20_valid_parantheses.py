"""
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(':
            stack.append(')')
        elif i == '[':
            stack.append(']')
        elif i == '{':
            stack.append('}')
        elif len(stack) == 0 or stack.pop() != i:
            return False
    return len(stack) == 0


def is_valid_2(s: str) -> bool:
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0
