# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM&status=TO_DO%2CATTEMPTED

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-math.inf] * (target + 1)
        dp[0] = 0
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = max(dp[i], dp[i - num] + 1)
        return dp[target] if dp[target] != -math.inf else -1
                
        