# https://leetcode.com/problems/is-subsequence/
class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize the memoization dictionary to store results of subproblems
        memo = {}

        # Define the recursive function that checks if s[i:] is a subsequence of t[j:]
        def is_subsequence_recursive(i, j):
            # If we have reached the end of s, return True (empty string is a subsequence of any string)
            if i == len(s):
                return True
            # If we have reached the end of t but not s, return False (not all characters of s are found)
            if j == len(t):
                return False
            # If the result for this subproblem is already computed, return it
            if (i, j) in memo:
                return memo[(i, j)]

            # If the current characters of s and t match, move to the next characters in both strings
            if s[i] == t[j]:
                memo[(i, j)] = is_subsequence_recursive(i + 1, j + 1)
            else:
                # If they don't match, move to the next character in t only and keep i same
                memo[(i, j)] = is_subsequence_recursive(i, j + 1)

            # Return the result for this subproblem
            return memo[(i, j)]

        # Start the recursion from the beginning of both strings
        return is_subsequence_recursive(0, 0)
