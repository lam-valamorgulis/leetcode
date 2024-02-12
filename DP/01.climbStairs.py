# https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
  def minCostClimbingStairs(self, cost):
      # Initialize an array to store the minimum cost to reach each step
      dp = [0] * (len(cost) + 1)

      # Base cases: The cost to reach the first and second steps
      dp[0] = cost[0]
      dp[1] = cost[1]

      # Iterate through the steps, calculating the minimum cost to reach each step
      for i in range(2, len(cost) + 1):
          # The minimum cost to reach the current step is the cost of the current step plus the minimum of the costs to reach the previous two steps
          dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

      # Return the minimum cost to reach the top, which is the last step
      return min(dp[-1], dp[-2])

# Example usage:
cost1 = [10, 15, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
sol = Solution()
print(sol.minCostClimbingStairs(cost1))  # Output: 15
print(sol.minCostClimbingStairs(cost2))  # Output: 6

