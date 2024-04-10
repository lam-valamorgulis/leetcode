# https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
      if matrix is None:
          return 0

      n = len(matrix)

      dp = [[0]* n for _ in range(n)]

      for j in range(n):
          dp[0][j] = matrix[0][j]

      for i in range(1,n):
          for j in range(n):
              dp[i][j] = matrix[i][j] + min(dp[i-1][max(0,j-1)], dp[i-1][j], dp[i-1][min(n-1,j+1)])

      return min(dp[-1])