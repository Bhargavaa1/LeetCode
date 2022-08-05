# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Runtime: O(N) Space: O(N)
# Hash Map Solution
def twoSum(nums: List[int], target: int) -> List[int]:
    numsDict = {}
    for i in range(len(nums)):
        if target-nums[i] in numsDict.keys():
            return [i, numsDict[target-nums[i]]]
        else:
            numsDict[nums[i]] = i
