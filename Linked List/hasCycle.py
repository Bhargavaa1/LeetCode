from typing import *
# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
class ListNode:
    def __init__(self, val:int = 0, next:Optional[ListNode] = None):
        self.val = val
        self.next = next

class Solution:
    # Hashset Solution
    # Runtime: O(N) Space: O(N)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        iter = head
        while iter:
            if iter in hashSet:
                return True
            else:
                hashSet.add(iter)
            iter = iter.next
        return False

    # Floyd’s Cycle Finding Algorithm
    # Runtime: O(N) Space: O(1)
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow,fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
            