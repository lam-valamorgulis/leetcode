# https://leetcode.com/problems/integer-break/


class Solution:

    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = -float('inf')
            for j in range(1, i):
                # Consider three cases:
                # 1. Existing maximum for dp[i]
                # 2. Product of j and (i - j) (direct split)
                # 3. Product of j and best product for dp[i - j] (recursive split)
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
