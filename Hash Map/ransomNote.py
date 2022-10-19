from typing import *
from collections import Counter
# 383. Ransom Note
# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    # Runtime: O(N) Space: O(1)
    # Character Counting Hash Map Solution
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict, magazineDict = {}, {}
        for i in ransomNote:
            if i not in ransomNoteDict:
                ransomNoteDict[i] = 1
            else:
                ransomNoteDict[i] += 1
        for j in magazine:
            if j not in magazineDict:
                magazineDict[j] = 1
            else:
                magazineDict[j] += 1
        for k in ransomNote:
            if k not in magazineDict or ransomNoteDict[k] > magazineDict[k]:
                return False
        return True

    # Runtime: O(N) Space: O(1)
    # Character Counting Counter Solution
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCharCounter, magazineCharCounter = Counter(ransomNote), Counter(magazine)
        for ransomNoteChar in ransomNoteCharCounter:
            if ransomNoteChar not in magazineCharCounter or magazineCharCounter[ransomNoteChar] < ransomNoteCharCounter[ransomNoteChar]:
                return False
        return True
