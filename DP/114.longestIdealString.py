# https://leetcode.com/problems/longest-ideal-subsequence/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
                # DP array to store the longest subsequence for each character
        dp = [0] * len(s)
        
        # Array to store the longest subsequence ending with a particular character (from 'a' to 'z')
        last_dp = [0] * 26
        
        for i in range(len(s)):
            # Get the alphabet index of the current character (0 for 'a', 25 for 'z')
            idx = ord(s[i]) - ord('a')
            
            # Start with a subsequence of just the current character
            max_len = 1
            
            # Check all valid previous characters within the range [s[i] - k, s[i] + k]
            for j in range(max(0, idx - k), min(25, idx + k) + 1):
                max_len = max(max_len, last_dp[j] + 1)
            
            # Update the DP for the current character
            dp[i] = max_len
            
            # Update last_dp for this character
            last_dp[idx] = max(last_dp[idx], dp[i])
        
        # The answer is the maximum value in the dp array
        return max(dp)
