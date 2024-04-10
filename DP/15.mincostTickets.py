# https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution:
  def mincostTickets(self, days: List[int], cost: List[int]) -> int:
      travel = set(days)
      # dp[i] = cost of travelling on all days before i and on i
      dp = [-1] * (days[-1] + 1)
      dp[0] = 0
      for d in range(1, days[-1] + 1):
          if d not in travel:
              dp[d] = dp[d - 1]
          else:
              dp[d] = min(dp[d - 1] + cost[0], 
                      dp[max(0, d - 7)] + cost[1],
                      dp[max(0, d - 30)] + cost[2])
      return dp[-1]