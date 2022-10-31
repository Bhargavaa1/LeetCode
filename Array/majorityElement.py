from typing import *
# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
class Solution:
    # Frequency Hashmap And Return The Element That Appears More Than N/2 times
    # Runtime: O(N) Space: O(N)
    def majorityElement(self, nums: List[int]) -> int:
        numsCount,n = {}, len(nums)
        for num in nums:
            if num not in numsCount.keys():
                numsCount[num] = 1
            else:
                numsCount[num] += 1
        for i in numsCount:
            if numsCount[i] > (n // 2):
                return i
        return -1
    
    # Boyer-Moore Algorithm
    # Runtime: O(N) Space: O(1)
    def majorityElement1(self, nums: List[int]) -> int:
        result,count = 0,0
        for num in nums:
            if count == 0:
                result = num
            if num == result:
                count += 1
            else:
                count -= 1
        return result
