from typing import *
# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(nums: List[int]) -> int:
        # Runtime: O(N) Space: O(1)
        # Kadane's Algorithm
        globalMax = nums[0]
        localMax = 0
        for num in nums:
            localMax = max(localMax+num, num)
            globalMax = max(globalMax, localMax)
        return globalMax
