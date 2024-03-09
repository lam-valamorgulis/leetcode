# https://leetcode.com/problems/unique-paths/

# Using Dynamic Programming (DP) is generally better than using Depth-First Search (DFS) for solving the unique paths problem for several reasons:

# Efficiency: Dynamic Programming offers a more efficient solution with a time complexity of O(m * n), where 'm' is the number of rows and 'n' is the number of columns in the grid. On the other hand, the DFS approach has an exponential time complexity of O(2^(m+n)), which becomes impractical for larger grids due to the sheer number of recursive calls.

# Avoidance of Redundant Computations: DP builds up the solution from smaller subproblems and stores the intermediate results in a table, avoiding redundant computations. In contrast, DFS explores all possible paths from the starting cell to the destination, resulting in redundant calculations for overlapping subproblems.

# Space Complexity: While both approaches use additional space for storing intermediate results, the space complexity of DP is O(m * n) for storing the DP table, which is acceptable for most practical purposes. On the other hand, DFS can have a high space complexity due to the recursive function calls and the associated stack space.

# Scalability: DP scales better for larger grids and can handle grid sizes that DFS cannot due to its exponential time complexity. As a result, DP is more suitable for real-world applications where efficiency and scalability are important considerations.

# Overall, while DFS is a valid approach for solving the unique paths problem, Dynamic Programming offers a more efficient and scalable solution, making it the preferred choice in most cases.


class Solution:

  def uniquePaths(self, m: int, n: int) -> int:
    # bottom up
    # init 2d grid
    dp = [[0] * n for _ in range(m)]

    # base case
    # each node of top right of grid or left of grid only one way to reach node
    for i in range(m):
      dp[i][0] = 1
    for j in range(n):
      dp[0][j] = 1

    # calculation add up to the destination base on base case:
    # The number of unique paths to cell (i, j) is the sum of paths
    # from the cell above and the cell to the left
    for r in range(1, m):
      for c in range(1, n):
        dp[r][c] = dp[r][c - 1] + dp[r - 1][c]

    return dp[m - 1][n - 1]
