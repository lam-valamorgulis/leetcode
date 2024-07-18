# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/


class Solution:

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n  # Initialize dp array with -1
        dp[0] = 0  # Starting point needs 0 jumps

        for i in range(n):
            if dp[i] != -1:  # If the index is reachable
                for j in range(i + 1, n):
                    if -target <= nums[j] - nums[i] <= target:
                        dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1]
