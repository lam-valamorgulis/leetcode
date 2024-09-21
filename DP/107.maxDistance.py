# https://leetcode.com/problem-list/dynamic-programming/?difficulty=MEDIUM

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        water_cells = 0

        # Step 1: Initialize the queue with all land cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))  # (row, col, distance)
                else:
                    water_cells += 1

        # If there's no water or no land, return -1
        if not queue or water_cells == 0:
            return -1

        max_distance = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2 & 3: Perform BFS and keep track of maximum distance
        while queue:
            row, col, distance = queue.popleft()
            max_distance = max(max_distance, distance)

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1  # Mark as visited
                    queue.append((new_row, new_col, distance + 1))

        # Step 4: Return the maximum distance
        return max_distance

