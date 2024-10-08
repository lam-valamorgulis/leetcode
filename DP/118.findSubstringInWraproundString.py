# https://leetcode.com/problems/unique-substrings-in-wraparound-string/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Array to store the maximum length of substrings ending with each letter
        dp = [0] * 26
        
        # Variable to track the length of the current valid consecutive substring
        current_length = 0
        
        for i in range(len(s)):
            # Check if current character and previous character are consecutive in the alphabet
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
                current_length += 1
            else:
                current_length = 1
            
            # Find the index of the current character in the alphabet
            index = ord(s[i]) - ord('a')
            
            # Update the dp array with the maximum length of substring ending with s[i]
            dp[index] = max(dp[index], current_length)
        
        # Sum of all dp values gives the number of unique substrings
        return sum(dp)

        