from typing import *
# 1480. Running Sum of 1d Array
# # Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# # Return the running sum of nums.
class Solution:
    # Using "Extra" Space
    # Runtime: O(N) Space complexity: O(1) [Input and Output Array Space does not count]
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = result[i-1]+nums[i]
        return result
    
    # In-place
    # Runtime: O(N) Space complexity: O(1) [Input and Output Array Space does not count]
    def runningSumInPlace(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i-1]+nums[i]
        return nums            

    
