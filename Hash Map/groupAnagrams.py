from typing import *
# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Runtime: O(N) Space: O(N)
# Sorting And Hashmap Solution


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagramCount = {}
    for i in strs:
        sortedI = ''.join(sorted(i))
        if sortedI in anagramCount.keys():
            anagramCount[sortedI].append(i)
        else:
            anagramCount[sortedI] = [i]
    return anagramCount.values()
