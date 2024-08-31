# https://leetcode.com/problems/best-team-with-no-conflicts/


class Solution:

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Pair up age and score, then sort primarily by age and secondarily by score
        players = sorted(zip(ages, scores))

        # DP array to store the maximum score for teams including the ith player
        n = len(players)
        dp = [0] * n

        # Start with each player's own score as the initial dp value
        for i in range(n):
            dp[i] = players[i][1]

        # Iterate through each player
        for i in range(n):
            for j in range(i):
                # If there's no conflict, update dp[i]
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        # The answer is the maximum value in the dp array
        return max(dp)
