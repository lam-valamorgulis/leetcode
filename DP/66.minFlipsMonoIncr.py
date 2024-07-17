#https://leetcode.com/problems/flip-string-to-monotone-increasing/


class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:

        n = len(s)
        # Initialize dp arrays
        dp0 = [0] * n
        dp1 = [0] * n

        # Initial state
        dp0[0] = 0 if s[0] == '0' else 1
        dp1[0] = 0 if s[0] == '1' else 1

        # Fill dp arrays
        for i in range(1, n):
            if s[i] == '0':
                dp0[i] = dp0[i - 1]
                dp1[i] = min(dp0[i - 1], dp1[i - 1]) + 1
            else:
                dp0[i] = dp0[i - 1] + 1
                dp1[i] = min(dp0[i - 1], dp1[i - 1])

        # The answer is the minimum flips required to make the entire string monotone increasing
        return min(dp0[n - 1], dp1[n - 1])
