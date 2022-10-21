from typing import *
from collections import Counter
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

class Solution:
    # Runtime: O(N log N) Space: O(N)
    # Sorted Solution
    def containsDuplicate1(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    # Runtime: O(1) Space: O(N)
    # HashSet Solution
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    # Runtime: O(N) Space: O(N)
    # Counter Solution Using Dictionary
    def containsDuplicate3(self, nums: List[int]) -> bool:
        numsCount = {}
        for num in nums:
            if num in numsCount.keys():
                return False
            numsCount[count] = 1
        return True

    # Runtime: O(N) Space: O(N)
    # Counter Solution
    def containsDuplicate4(self, nums: List[int]) -> bool:
        numsCount = Counter(nums)
        for num in numsCount.keys():
            if numsCount[num] != 1:
                return False
        return True
