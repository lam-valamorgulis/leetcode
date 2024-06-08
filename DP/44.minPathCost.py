# https://leetcode.com/problems/minimum-path-cost-in-a-grid/


class Solution:

    def minPathCost(self, grid: List[List[int]],
                    moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(x, y):
            # If we are in the last row, return the value of the cell
            if x == m - 1:
                return grid[x][y]

            # Check if the result is already computed
            if (x, y) in memo:
                return memo[(x, y)]

            # Initialize the minimum cost as infinity
            min_cost = float('inf')

            # Calculate the cost for each cell in the next row
            for k in range(n):
                next_cost = grid[x][y] + moveCost[grid[x][y]][k] + dfs(
                    x + 1, k)
                min_cost = min(min_cost, next_cost)

            # Cache the result
            memo[(x, y)] = min_cost
            return min_cost

        # Start from each cell in the first row and find the minimum path cost
        min_path_cost = float('inf')
        for j in range(n):
            min_path_cost = min(min_path_cost, dfs(0, j))

        return min_path_cost
