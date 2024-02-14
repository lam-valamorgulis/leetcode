# https://leetcode.com/problems/house-robber-ii/


class Solution(object):

  def rob(self, nums):
    if len(nums) == 1:
      return nums[0]

    # Define a helper function to calculate the maximum amount of money that can be robbed
    def rob_houses(nums):
      if not nums:
        return 0
      if len(nums) == 1:
        return nums[0]

      dp = [0] * len(nums)
      dp[0] = nums[0]
      dp[1] = max(nums[0], nums[1])

      for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

      return dp[-1]

    # Calculate the maximum amount of money that can be robbed starting from the first house and excluding the last house
    max_amount1 = rob_houses(nums[:-1])

    # Calculate the maximum amount of money that can be robbed starting from the second house and excluding the first house
    max_amount2 = rob_houses(nums[1:])

    # Return the maximum of the two amounts calculated above
    return max(max_amount1, max_amount2)
