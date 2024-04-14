# https://leetcode.com/problems/triangle/


class Solution:

  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # Define a helper function for recursion with memoization
    def min_path(row: int, col: int, memo: dict) -> int:
      # If we have reached the bottom of the triangle
      if row == len(triangle) - 1:
        return triangle[row][col]

      # If the result for the current position is already memoized
      if (row, col) in memo:
        return memo[(row, col)]

      # Recursively compute the minimum path sum for the next row
      left_sum = min_path(row + 1, col, memo)
      right_sum = min_path(row + 1, col + 1, memo)

      # Memoize the result and return
      memo[(row, col)] = triangle[row][col] + min(left_sum, right_sum)
      return memo[(row, col)]

    # Start the recursion from the top of the triangle
    return min_path(0, 0, {})
