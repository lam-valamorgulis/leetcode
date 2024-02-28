# https://leetcode.com/problems/rotting-oranges/

# The code aims to find the minimum time required for all oranges to rot using the BFS algorithm.
# It initializes a deque to store the coordinates of rotten oranges and tracks the count of fresh oranges and time taken.
# It iterates through the grid to count fresh oranges and add rotten oranges' coordinates to the queue.
# It defines directions for moving in the grid (up, down, left, right).
# It performs BFS while there are fresh oranges and the queue is not empty.
# In each iteration, it pops a rotten orange from the queue and checks its adjacent cells.
# If an adjacent cell contains a fresh orange, it makes it rotten, adds its coordinates to the queue, and decrements the count of fresh oranges.
# It returns the time taken if all fresh oranges have been rotten, otherwise returns -1.


class Solution:

  def orangesRotting(self, grid):
    q = collections.deque(
    )  # Initialize a deque to store coordinates of rotten oranges
    fresh = 0  # Initialize a variable to count the number of fresh oranges
    time = 0  # Initialize a variable to track the time taken

    # Iterate through the grid to count fresh oranges and add rotten oranges to the queue
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == 1:  # If the orange is fresh
          fresh += 1  # Increment the count of fresh oranges
        if grid[r][c] == 2:  # If the orange is rotten
          q.append((r, c))  # Add its coordinates to the queue

    directions = [[0, 1], [0, -1], [1, 0],
                  [-1, 0]]  # Define directions for moving in the grid

    # Perform BFS while there are fresh oranges and the queue is not empty
    while fresh > 0 and q:
      length = len(q)
      for i in range(length):
        r, c = q.popleft()  # Get the coordinates of the rotten orange

        # Iterate through each adjacent cell
        for dr, dc in directions:
          row, col = r + dr, c + dc
          # Check if the adjacent cell is within the grid bounds and contains a fresh orange
          if (row in range(len(grid)) and col in range(len(grid[0]))
              and grid[row][col] == 1):
            grid[row][col] = 2  # Make the orange rotten
            q.append((row, col))  # Add its coordinates to the queue
            fresh -= 1  # Decrement the count of fresh oranges

      time += 1  # Increment the time

    # Return the time taken if all fresh oranges have been rotten, otherwise return -1
    return time if fresh == 0 else -1
