# https://leetcode.com/problems/out-of-boundary-paths/


class Solution:

  def findPaths(self, m: int, n: int, maxMove: int, startRow: int,
                startColumn: int) -> int:
    MOD = 10**9 + 7
    memo = {}

    def dfs(x, y, move):
      # If the ball is out of boundary
      if x < 0 or x >= m or y < 0 or y >= n:
        return 1
      # If the maximum move is used up
      if move == 0:
        return 0
      # If already calculated, return from memo
      if (x, y, move) in memo:
        return memo[(x, y, move)]

      # Define directions
      directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
      paths = 0

      for dx, dy in directions:
        nx, ny = x + dx, y + dy
        paths += dfs(nx, ny, move - 1)

      # Update memo and return paths modulo MOD
      memo[(x, y, move)] = paths % MOD
      return memo[(x, y, move)]

      # Start DFS from the initial position

    return dfs(startRow, startColumn, maxMove)
