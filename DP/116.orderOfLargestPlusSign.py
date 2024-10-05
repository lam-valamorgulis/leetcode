# https://leetcode.com/problems/largest-plus-sign/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Create a set of mine positions for O(1) lookup
        mine_set = set(map(tuple, mines))
        
        # Initialize dp array
        dp = [[0] * n for _ in range(n)]
        
        # Initialize result
        result = 0
        
        # Compute left and right arms
        for r in range(n):
            # Left to right
            count = 0
            for c in range(n):
                count = 0 if (r, c) in mine_set else count + 1
                dp[r][c] = count
            
            # Right to left
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in mine_set else count + 1
                dp[r][c] = min(dp[r][c], count)
        
        # Compute top and bottom arms, and update result
        for c in range(n):
            # Top to bottom
            count = 0
            for r in range(n):
                count = 0 if (r, c) in mine_set else count + 1
                dp[r][c] = min(dp[r][c], count)
            
            # Bottom to top
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in mine_set else count + 1
                dp[r][c] = min(dp[r][c], count)
                result = max(result, dp[r][c])
        
        return result