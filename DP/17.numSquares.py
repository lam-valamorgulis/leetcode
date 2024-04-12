# https://leetcode.com/problems/perfect-squares/


class Solution:
  def numSquares(self, n: int) -> int:
      # Initialize DP array with maximum values
      dp = [float('inf')] * (n + 1)

      # Base case: 0 requires 0 perfect squares
      dp[0] = 0

      # Iterate through all numbers from 1 to n
      for i in range(1, n + 1):
          # Try all possible perfect square numbers up to sqrt(i)
          j = 1
          while j * j <= i:
              dp[i] = min(dp[i], dp[i - j * j] + 1)
              j += 1

      return dp[n]