# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        res = 0
        i = 1
        N = len(word)
        while i < N:
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                res += 1
                i += 1
            i += 1
        return res