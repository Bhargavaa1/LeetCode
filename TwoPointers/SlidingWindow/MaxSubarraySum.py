# Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.
# For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.
# About subarrays or substrings -> Dealswith sums or additive -> Sliding Window
from typing import List


def max_subarray_sum(nums: List[int], k: int) -> int:
  window_sum = 0
  for i in range(k):
    window_sum += nums[i]
  max_sum = window_sum
  for r in range(k, len(nums)):
    l = r - k
    window_sum -= nums[l]
    window_sum += nums[r]
    max_sum = max(max_sum, window_sum)
  return max_sum
