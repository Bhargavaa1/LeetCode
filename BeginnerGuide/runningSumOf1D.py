from typing import *
# 1480. Running Sum of 1d Array
# # Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# # Return the running sum of nums.
class Solution:
    # Caching
    # Runtime: O(N) Space complexity: O(N)
    def  runningSum(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = result[i-1]+nums[i]
        return result