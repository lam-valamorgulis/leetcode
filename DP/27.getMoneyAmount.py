# https://leetcode.com/submissions/detail/1252735897/


class Solution:

  def getMoneyAmount(self, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
      for start in range(1, n - length + 2):
        end = start + length - 1
        dp[start][end] = min(guess +
                             max(dp[start][guess - 1], dp[guess + 1][end])
                             for guess in range(start, end))
    return dp[1][n]
