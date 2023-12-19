"""
Design a Skiplist without using any built-in libraries.

A skiplist is a data structure that takes O(log(n)) time to add, erase and
search. Comparing with treap and red-black tree which has the same function
and performance, the code length of Skiplist can be comparatively short and
the idea behind Skiplists is just simple linked lists.
"""
import random


class Node:
    __slots__ = ('val', 'next', 'down')

    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:
    MAX_LEVEL = 16

    def __init__(self):
        node = Node(float('-inf'))
        node.next = Node(float('inf'))
        self.levels = [node]

    def search(self, target: int) -> bool:
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < target:
                node = node.next
            if node.next.val == target:
                return True
            level = node.down
        return False

    def add(self, num: int) -> None:
        stack_of_prevs = []
        stack_of_nexts = []
        current_level = self.levels[-1]
        while current_level:
            current = current_level
            while current.next.val < num:
                current = current.next
            stack_of_prevs.append(current)
            stack_of_nexts.append(current.next)
            current_level = current.down

        increase_level = True
        down = None
        while stack_of_prevs and increase_level:
            prev = stack_of_prevs.pop()
            new_node = Node(num)
            next = stack_of_nexts.pop()
            prev.next = new_node
            new_node.next = next
            new_node.down = down
            down = new_node

            increase_level = random.randint(0, 1)

        if not stack_of_prevs and increase_level \
                and len(self.levels) < self.MAX_LEVEL:
            new_head = Node(float('-inf'))
            new_node = Node(num)
            new_head.next = new_node
            new_node.next = Node(float('inf'))
            new_head.down = self.levels[-1]
            new_node.down = down
            self.levels.append(new_head)

    def erase(self, num: int) -> bool:
        stack = []
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            if node.next.val == num:
                stack.append(node)
            level = node.down

        if not stack:
            return False

        for node in stack:
            node.next = node.next.next

        while len(self.levels) > 1 and self.levels[-1].next.next is None:
            self.levels.pop()

        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
