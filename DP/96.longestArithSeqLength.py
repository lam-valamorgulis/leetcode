# https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        max_length = 0

        for i in range(len(nums)):
            dp[i] = {}
            for j in range(i):
                d = nums[i] - nums[j]
                if d in dp[j]:
                    dp[i][d] = dp[j][d] + 1
                else:
                    dp[i][d] = 2
                max_length = max(max_length, dp[i][d])

        return max_length
