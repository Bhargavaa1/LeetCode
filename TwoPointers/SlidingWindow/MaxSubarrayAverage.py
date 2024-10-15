# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10^-5 will be accepted.
from typing import List

def find_max_average(nums: List[int], k: int) -> float:
  window_sum= 0.0
  for i in range(k):
    window_sum += nums[i]
  result = window_sum/k
  for r in range(k, len(nums)):
    l = r-k
    window_sum -= nums[l]
    window_sum += nums[r]
    result = max(result, (window_sum/k))
  return result

