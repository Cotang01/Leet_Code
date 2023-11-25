"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge_two_lists(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        while head_1 and head_2:
            if head_1.val < head_2.val:
                current.next = head_1
                head_1 = head_1.next
            else:
                current.next = head_2
                head_2 = head_2.next
            current = current.next
        if head_1 or head_2:
            current.next = head_1 if head_1 else head_2
        return head.next
