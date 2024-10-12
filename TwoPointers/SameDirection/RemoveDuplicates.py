# Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.
# Input: [0, 0, 1, 1, 1, 2, 2]
# Output: 3
# O(1) Memory Required -> Involves Monotonic Condition -> Two Pointers
from typing import List


def remove_duplicates(nums: List[int]) -> int:
  s = 0
  for f in range(nums):
    if nums[s] != nums[f]:
      s += 1
      nums[s] = nums[f]
  return s + 1
