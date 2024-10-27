# https://leetcode.com/problems/maximum-earnings-from-taxi/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM&status=TO_DO%2CATTEMPTED

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort rides by end point for efficient processing
        rides.sort(key=lambda x: x[1])
        
        # dp[i] represents the maximum earnings possible up to point i
        dp = [0] * (n + 1)
        
        # Keep track of current ride being processed
        j = 0
        
        # Process each point from 1 to n
        for i in range(1, n + 1):
            # Copy over earnings from previous point
            dp[i] = dp[i - 1]
            
            # Process all rides that end at current point i
            while j < len(rides) and rides[j][1] == i:
                start, end, tip = rides[j]
                # Earnings = distance + tip + maximum earnings up to start point
                earnings = end - start + tip + dp[start]
                # Update maximum earnings at current point if this is better
                dp[i] = max(dp[i], earnings)
                j += 1
        
        return dp[n]