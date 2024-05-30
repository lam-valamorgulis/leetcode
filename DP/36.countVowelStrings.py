#https://leetcode.com/problems/count-sorted-vowel-strings/


# Definition for a binary tree node.
class Solution:

    def countVowelStrings(self, n: int) -> int:
        memo = {}

        def countStrings(length, last_vowel):
            if length == 0:
                return 1
            if (length, last_vowel) in memo:
                return memo[(length, last_vowel)]

            count = 0
            for vowel in range(last_vowel + 1):
                count += countStrings(length - 1, vowel)

            memo[(length, last_vowel)] = count
            return count

        return countStrings(n, 4)  # Start with 'u' as the last vowel
