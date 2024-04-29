# https://leetcode.com/problems/unique-paths-ii/


class Solution:

  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    # Get the dimensions of the grid
    m = len(obstacleGrid)  # Number of rows
    n = len(obstacleGrid[0])  # Number of columns

    # Initialize the dp array with zeros
    dp = [[0] * n for _ in range(m)]

    # Base case: If the starting cell is not an obstacle, there is one way to reach it
    dp[0][0] = int(obstacleGrid[0][0] == 0)

    # Update the number of paths for the first column
    for i in range(1, m):
      # If the current cell is not an obstacle and we can reach it from the top cell
      dp[i][0] = int(obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1)

    # Update the number of paths for the first row
    for j in range(1, n):
      # If the current cell is not an obstacle and we can reach it from the left cell
      dp[0][j] = int(obstacleGrid[0][j] == 0 and dp[0][j - 1] == 1)

    # Update the number of paths for the rest of the grid
    for i in range(1, m):
      for j in range(1, n):
        # If the current cell is not an obstacle, add the number of paths from the top and from the left
        if obstacleGrid[i][j] == 0:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Return the number of paths to the bottom-right cell
    return dp[m - 1][n - 1]
