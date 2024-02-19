# https://leetcode.com/problems/number-of-islands/

# We define a nested function dfs to perform Depth-First Search from a given cell (i, j).
# We iterate through each cell in the grid, and whenever we encounter a land cell ('1'), we start DFS from that cell.
# During DFS, we explore all neighboring land cells and mark them as visited by changing their value to '0'.
# We count the number of times we start DFS, which corresponds to the number of islands in the grid.
# Finally, we return the count of islands.


def numIslands(grid):
  if not grid:
    return 0

  def dfs(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(
        grid[0]) or grid[i][j] == '0':
      return
    grid[i][j] = '0'  # Mark the current cell as visited
    # Explore neighboring cells
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

  num_islands = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '1':
        num_islands += 1
        dfs(i, j)  # Explore the island
  return num_islands


# Example usage:
grid1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(numIslands(grid1))  # Output: 1

grid2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(numIslands(grid2))  # Output: 3
