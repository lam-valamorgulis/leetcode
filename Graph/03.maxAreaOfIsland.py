# https://leetcode.com/problems/max-area-of-island/

# Understand the Problem: The problem asks us to find the maximum area of an island in a given 2D grid, where an island is a group of connected '1' cells (representing land) surrounded by '0' cells (representing water). We need to find the area of the largest island in the grid.
# Identify the Problem as a Graph: We can model the given grid as a graph where each cell represents a node, and edges connect adjacent land cells. We can then use depth-first search (DFS) to traverse the graph and explore each connected component (island) to find its area.
# Design the DFS Function: We'll design a recursive DFS function that explores the grid starting from a given cell. The DFS function will recursively visit neighboring land cells and mark them as visited to avoid revisiting. We'll keep track of the area of the current island during traversal.
# Apply DFS to Each Cell: We'll iterate through each cell in the grid. If we encounter a land cell ('1') that has not been visited, we'll initiate a DFS traversal from that cell to explore the connected island and calculate its area. We'll keep track of the maximum area found so far.
# Time Complexity Analysis: The time complexity of DFS applied to each cell in the grid is O(N * M), where N is the number of rows and M is the number of columns in the grid. This is because we traverse each cell only once.
# Space Complexity Analysis: The space complexity is O(N * M) as well, considering the recursion stack space and the visited array.
# Implement and Test: Finally, we'll implement the solution based on the above approach and test it with various test cases to ensure correctness and efficiency.


class Solution(object):

  def maxAreaOfIsland(self, grid):

    def dfs(i, j):
      if i < 0 or i >= len(grid) or j < 0 or j >= len(
          grid[0]) or grid[i][j] == 0:
        return 0

      # Mark the current cell as visited by changing its value to 0
      grid[i][j] = 0

      # Calculate the area of the island including the current cell
      area = 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
      return area

    max_area = 0
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == 1:
          area = dfs(r, c)
          max_area = max(max_area, area)
    return max_area
