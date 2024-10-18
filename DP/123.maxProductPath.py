# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] stores tuple of (max_product, min_product) reaching cell (i,j)
        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]
        
        # Initialize first cell
        dp[0][0] = (grid[0][0], grid[0][0])
        
        # Initialize first row
        for j in range(1, n):
            curr = grid[0][j]
            prev_max, prev_min = dp[0][j-1]
            dp[0][j] = (curr * prev_max, curr * prev_min) if curr >= 0 else (curr * prev_min, curr * prev_max)
        
        # Initialize first column
        for i in range(1, m):
            curr = grid[i][0]
            prev_max, prev_min = dp[i-1][0]
            dp[i][0] = (curr * prev_max, curr * prev_min) if curr >= 0 else (curr * prev_min, curr * prev_max)
        
        # Fill the rest of dp table
        for i in range(1, m):
            for j in range(1, n):
                curr = grid[i][j]
                # Get max and min from top cell and left cell
                top_max, top_min = dp[i-1][j]
                left_max, left_min = dp[i][j-1]
                
                if curr >= 0:
                    # If current number is positive, max comes from max and min from min
                    max_prod = max(curr * top_max, curr * left_max)
                    min_prod = min(curr * top_min, curr * left_min)
                else:
                    # If current number is negative, max comes from min and min from max
                    max_prod = max(curr * top_min, curr * left_min)
                    min_prod = min(curr * top_max, curr * left_max)
                
                dp[i][j] = (max_prod, min_prod)
        
        # Get the maximum product at bottom-right cell
        max_product = dp[m-1][n-1][0]
        
        return max_product % MOD if max_product >= 0 else -1

        
