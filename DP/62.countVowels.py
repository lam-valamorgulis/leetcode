# https://leetcode.com/problems/vowels-of-all-substrings/


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        total_vowels = 0

        for i in range(n):
            if word[i] in vowels:
                # Substrings starting from the beginning to the current position
                left = i + 1
                # Substrings ending from the current position to the end
                right = n - i
                # Each vowel contributes to left * right substrings
                total_vowels += left * right

        return total_vowels

