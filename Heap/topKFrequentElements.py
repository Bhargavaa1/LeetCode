from typing import *
from collections import Counter
# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

class Solution:
    # Count Frequency of Elements and Sort
    # Runtime: O(N log N) Space: O(N)
    def topKFrequentSortCount(self, nums: List[int], k:int) -> List[int]:
        numsCount = {}
        for num in nums:
            numsCount[num] = numsCount.get(num,0)
        sortedNumsCount = sorted(numsCount, key = numsCount.get, reverse = True)
        return sortedNumsCount[0:k]
    
    # Heap Solution