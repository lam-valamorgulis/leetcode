# https://leetcode.com/problems/knight-dialer/

class Solution:
  def knightDialer(self, n: int) -> int:
      # Define the mod value
      mod = 10**9 + 7

      # Valid knight moves from each digit
      moves = {
          0: [4, 6],
          1: [6, 8],
          2: [7, 9],
          3: [4, 8],
          4: [0, 3, 9],
          5: [],
          6: [0, 1, 7],
          7: [2, 6],
          8: [1, 3],
          9: [2, 4]
      }

      # Initialize dp array
      dp = [[0] * 10 for _ in range(n)]
      for j in range(10):
          dp[0][j] = 1

      # Fill dp array
      for i in range(1, n):
          for j in range(10):
              for move in moves[j]:
                  dp[i][j] += dp[i - 1][move]
                  dp[i][j] %= mod

      # Sum up the values in the last row of dp array
      return sum(dp[-1]) % mod

