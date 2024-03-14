# https://leetcode.com/problems/target-sum/


class Solution:

  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    n = len(nums)
    dp = [{} for _ in range(n)]

    def dfs(index, cur_sum):
      if index == n:
        if cur_sum == target:
          return 1
        else:
          return 0

      if cur_sum in dp[index]:
        return dp[index][cur_sum]

      positive = dfs(index + 1, cur_sum + nums[index])
      negative = dfs(index + 1, cur_sum - nums[index])

      dp[index][cur_sum] = positive + negative
      return dp[index][cur_sum]

    return dfs(0, 0)
