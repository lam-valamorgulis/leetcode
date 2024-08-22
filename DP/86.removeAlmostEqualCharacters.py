# https://leetcode.com/problems/count-submatrices-with-all-ones/


class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        # Step 1: Calculate the number of consecutive 1's horizontally for each cell
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    # Calculate the number of consecutive 1's horizontally ending at mat[i][j]
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1

        # Step 2: Calculate the number of submatrices ending at each cell (i, j)
        total_submatrices = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    # Track the minimum width in the current column to calculate submatrices
                    min_width = dp[i][j]
                    for k in range(i, -1, -1):  # Move upwards in the column
                        min_width = min(min_width, dp[k][j])
                        if min_width == 0:
                            break
                        total_submatrices += min_width

        return total_submatrices
