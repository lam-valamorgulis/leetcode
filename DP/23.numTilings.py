# https://leetcode.com/problems/domino-and-tromino-tiling/


class Solution:

  def numTilings(self, n: int) -> int:
    # Define the modulo value
    mod = 10**9 + 7

    # Initialize the dp array with zeros
    dp = [0] * (n + 1)
    # Base cases
    dp[0] = dp[1] = 1
    # Loop through the dp array starting from index 2
    for i in range(2, n + 1):
      # Calculate the next value in the dp array
      # based on the recurrence relation:
      # dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod
      dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod

    # Return the result for n
    return dp[n]
