# https://leetcode.com/problems/divisor-game/



class Solution:

    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        # Base cases
        if n >= 1:
            dp[1] = False  # Alice loses if the number is 1

        # Fill the DP array
        for i in range(2, n + 1):
            # Check all possible moves for Alice
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break

        # The result for the original number n
        return dp[n]
