# Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the
# non-zero elements. Do this in-place using constant auxillary space.
# O(1) Memory Required -> Involves Monotonic Conditions -> Two Pointers

from typing import List


def move_zeros(nums: List[int]) -> None:
  slow = 0
  for fast in range(len(move_zeros)):
    if nums[fast] != 0:
      nums[slow], nums[fast] = nums[fast], nums[slow]
      slow += 1
