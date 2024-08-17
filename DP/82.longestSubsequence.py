# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}  # Initialize dictionary to track subsequence lengths
        max_length = 0  # Variable to store the maximum subsequence length

        for x in arr:
            # If the previous element exists in dp, extend the subsequence
            if x - difference in dp:
                dp[x] = dp[x - difference] + 1
            else:
                dp[x] = 1  # Otherwise, start a new subsequence with x

            # Update the maximum length found so far
            max_length = max(max_length, dp[x])

        return max_length
