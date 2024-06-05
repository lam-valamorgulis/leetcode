# https://leetcode.com/problems/stone-game-ii/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i: int, j: int) -> int:
            # If this subproblem has been computed before, return the stored result
            if (i, j) in memo:
                return memo[(i, j)]

            # Base case: if we reach the end of either string, 
            # the number of operations is the number of remaining characters in the other string
            if i == len(word1) or j == len(word2):
                return max(len(word1) - i, len(word2) - j)

            # If the characters match, move on to the next characters in both strings
            if word1[i] == word2[j]:
                ans = dp(i + 1, j + 1)
            else:
                # If the characters don't match, try deleting a character from either string
                # and take the minimum number of operations
                ans = min(dp(i + 1, j), dp(i, j + 1)) + 1

            # Store the result of this subproblem
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)



