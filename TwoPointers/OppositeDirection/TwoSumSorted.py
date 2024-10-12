# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
# O(1) Memory Required -> Involves Monotonic Condition -> Two Pointers
from typing import List


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
  l, r = 0, len(nums) - 1
  two_sum: int = nums[l] + nums[r]
  while True:
    if two_sum == target:
      return [l + 1, r + 1]
    elif two_sum < target:
      l += 1
    else:
      r -= 1
