# https://leetcode.com/problems/solving-questions-with-brainpower/


class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            # Option 1: Solve the current question
            solve = questions[i][0] + dp(i + questions[i][1] + 1)
            # Option 2: Skip the current question
            skip = dp(i + 1)

            memo[i] = max(solve, skip)
            return memo[i]

        return dp(0)
