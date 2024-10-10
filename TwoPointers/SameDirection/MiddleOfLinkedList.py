# Find the middle node of a linked list. If the number of nodes is even, then return the second middle node
# Involves Linked Lists -> Two Pointers


class Node:
  def __init__(self, val: int, next=None):
    self.val = val
    self.next = next


def middle_of_linked_list(head: Node) -> int:
  slow = fast = head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  return slow.val
