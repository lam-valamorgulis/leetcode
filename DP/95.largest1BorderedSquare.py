# https://leetcode.com/problems/largest-1-bordered-square/

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Initialize DP arrays
        dp_left = [[0] * n for _ in range(m)]
        dp_up = [[0] * n for _ in range(m)]

        max_square_len = 0

        # Fill the DP arrays
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp_left[i][j] = dp_left[i][j-1] + 1 if j > 0 else 1
                    dp_up[i][j] = dp_up[i-1][j] + 1 if i > 0 else 1

                    # Check the maximum possible square ending at (i, j)
                    small_side = min(dp_left[i][j], dp_up[i][j])

                    while small_side > max_square_len:
                        if dp_left[i-small_side+1][j] >= small_side and dp_up[i][j-small_side+1] >= small_side:
                            max_square_len = small_side
                        small_side -= 1

        return max_square_len ** 2

