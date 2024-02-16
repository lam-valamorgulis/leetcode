# https://leetcode.com/problems/coin-change/description/


class Solution(object):

  def coinChange(self, coins, amount):
    # Initialize a dp array to store the minimum number of coins needed for each amount from 0 to amount
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Iterate through each amount from 1 to amount
    for i in range(1, amount + 1):
      # Try using each coin denomination to make up the current amount
      for coin in coins:
        # Check if the current coin denomination can be used to make up the amount i
        if i - coin >= 0:
          # Update dp[i] with the minimum of the current value of dp[i] and 1 + dp[i - coin]
          dp[i] = min(dp[i], 1 + dp[i - coin])

    # If dp[amount] is still infinity, it means no combination of coins can make up the amount
    return dp[amount] if dp[amount] != float('inf') else -1
