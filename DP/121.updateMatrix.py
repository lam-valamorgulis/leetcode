# https://leetcode.com/problems/01-matrix/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        visited = set()

        # Step 1: Add all 0s to the queue and mark them as visited
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        # Step 2: BFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    mat[nx][ny] = mat[x][y] + 1
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        return mat

        