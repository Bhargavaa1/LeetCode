# Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the
# non-zero elements. Do this in-place using constant auxillary space.
# O(1) Memory Required -> Involves Monotonic Conditions -> Two Pointers
# Time Complexity: O(N) Space Complexity: O(1)
from typing import List


def move_zeros(nums: List[int]) -> None:
  s = 0
  for f in range(len(move_zeros)):
    if nums[f] != 0:
      nums[s], nums[f] = nums[f], nums[s]
      s += 1
