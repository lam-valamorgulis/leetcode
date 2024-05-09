# https://leetcode.com/problems/longest-palindromic-subsequence/


class Solution:

  def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    # Initialize a 2D array dp with dimensions (n x n)
    dp = [[0] * n for _ in range(n)]

    # Fill the diagonal with 1, as the longest palindromic subsequence for substrings of length 1 is always 1
    for i in range(n):
      dp[i][i] = 1

    # Fill the table diagonally
    for l in range(2, n + 1):
      for i in range(n - l + 1):
        j = i + l - 1
        # If the characters at positions i and j are equal, then dp[i][j] = 2 + dp[i+1][j-1]
        if s[i] == s[j]:
          dp[i][j] = 2 + dp[i + 1][j - 1]
        # Otherwise, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        else:
          dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Return the length of the longest palindromic subsequence in the entire string s
    return dp[0][n - 1]
