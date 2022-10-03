from typing import *
# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = 0
        self.next = None

class Solution:
    # Two Pointer Solution with Dummy Node
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        solution = ListNode()
        itr = solution 
        while list1 and list2:
            if list1.val < list2.val:
                itr.next = list1
                list1 = list1.next
            else:
                itr.next = list2
                list2 = list2.next
            itr = itr.next
        if list1:
            itr.next = list1
        if list2:
            itr.next = list2
        return solution.next

