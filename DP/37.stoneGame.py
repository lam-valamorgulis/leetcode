# https://leetcode.com/problems/stone-game/submissions/1276116581/


class Solution(object):
    def stoneGame(self, piles):
         # The memoization cache to be filled up with subproblem solutions
        memo = {}

        # The helper function takes two pointers, i and j, which represent the current range of piles
        def dp(i, j):
            # If this subproblem has been solved before, return the solution
            if (i, j) in memo:
                return memo[(i, j)]

            # If there's only one pile left, return its value
            if i == j:
                return piles[i]

            # Calculate the score if Alice takes the pile at position i or j
            # The score is the value of the pile minus the score that Bob would get from the remaining piles
            # Since Bob also plays optimally, he would get the maximum score from the remaining piles
            pick_i = piles[i] - dp(i + 1, j)
            pick_j = piles[j] - dp(i, j - 1)

            # Alice's score is the maximum of the two options
            result = max(pick_i, pick_j)

            # Store the solution in the memoization cache
            memo[(i, j)] = result

            return result

        # Call the helper function with the initial range of piles
        total = dp(0, len(piles) - 1)

        # Alice wins if her total score is greater than 0
        return total > 0