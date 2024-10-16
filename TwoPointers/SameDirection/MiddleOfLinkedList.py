# Find the middle node of a linked list. If the number of nodes is even, then return the second middle node
# Involves Linked Lists -> Two Pointers
# Time Complexity: O(N) Space Complexity: O(1)


class Node:
  def __init__(self, val: int, next=None):
    self.val = val
    self.next = next


def middle_of_linked_list(head: Node) -> int:
  s = f = head
  while f and f.next:
    f = f.next.next
    s = s.next
  return s.val
