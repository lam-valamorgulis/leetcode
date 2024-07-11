# https://leetcode.com/problems/minimum-sideway-jumps/


class Solution:

    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        # Initialize the jumps needed to reach each lane at the starting position
        # Lane 1: 1 jump needed (from lane 2 to lane 1)
        # Lane 2: 0 jumps needed (starting lane)
        # Lane 3: 1 jump needed (from lane 2 to lane 3)
        dp = [1, 0, 1]

        for i in range(1, n + 1):
            # Update the current state considering the obstacles
            if obstacles[i] == 1:
                dp[0] = float('inf')
            elif obstacles[i] == 2:
                dp[1] = float('inf')
            elif obstacles[i] == 3:
                dp[2] = float('inf')

            # Calculate the minimum jumps needed for each lane by checking other lanes
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[j] = min(dp[j],
                                min(dp[(j + 1) % 3], dp[(j + 2) % 3]) + 1)

        return min(dp)
