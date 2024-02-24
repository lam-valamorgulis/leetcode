# https://leetcode.com/problems/surrounded-regions/


class Solution(object):

  def solve(self, board):

    rows, cols = len(board), len(board[0])

    def dfs(i, j):
      if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != "O":
        return False

      board[i][j] = "#"  # Mark as visited
      result = True

      # Explore neighbors
      result &= dfs(i + 1, j)
      result &= dfs(i - 1, j)
      result &= dfs(i, j + 1)
      result &= dfs(i, j - 1)

      return result

    for i in range(rows):
      for j in range(cols):
        if (i == 0 or i == rows - 1 or j == 0
            or j == cols - 1) and board[i][j] == "O":
          dfs(i, j)

    for i in range(rows):
      for j in range(cols):
        if board[i][j] == "O":
          board[i][j] = "X"
        elif board[i][j] == "#":
          board[i][j] = "O"

    return board
