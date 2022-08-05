# 383. Ransom Note
# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Runtime: O(N) Space: O(1)
# Character Counting Hash Map Solution
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    ransomNoteCharCounter, magazineCharCounter = {}, {}
    for i in ransomNote:
        if i in ransomNoteCharCounter:
            ransomNoteCharCounter[i] += 1
        else:
            ransomNoteCharCounter[i] = 1
    for i in magazine:
        if i in magazineCharCounter:
            magazineCharCounter[i] += 1
        else:
            magazineCharCounter[i] = 1
    for i in ransomNoteCharCounter:
        if i not in magazineCharCounter or magazineCharCounter[i] < ransomNoteCharCounter[i]:
            return False
    return True
