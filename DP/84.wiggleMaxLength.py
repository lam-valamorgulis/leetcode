# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/


class Solution:

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i] represents whether the subarray nums[0:i+1] can be validly partitioned.
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: an empty subarray can be considered valid

        for i in range(1, n):
            # Check if the last two elements form a valid subarray
            if i >= 1 and nums[i] == nums[i - 1]:
                dp[i + 1] = dp[i + 1] or dp[i - 1]

            # Check if the last three elements form a valid subarray
            if i >= 2:
                if nums[i] == nums[i - 1] == nums[i - 2]:
                    dp[i + 1] = dp[i + 1] or dp[i - 2]
                elif nums[i] == nums[i - 1] + 1 and nums[i -
                                                         1] == nums[i - 2] + 1:
                    dp[i + 1] = dp[i + 1] or dp[i - 2]

        return dp[n]
