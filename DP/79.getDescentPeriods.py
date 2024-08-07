# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                dp[i] += dp[i - 1]
        return sum(dp)
