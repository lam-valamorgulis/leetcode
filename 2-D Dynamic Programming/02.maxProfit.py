# https://leetcode.com/problems/longest-common-subsequence/

# Understanding the Problem: First, we need to understand what a longest common subsequence (LCS) is. Given two strings text1 and text2, an LCS is the longest sequence of characters that appears in both strings in the same relative order but not necessarily contiguous. Our goal is to find the length of the LCS.

# Dynamic Programming Approach: Dynamic programming is a technique used to solve problems by breaking them down into smaller overlapping subproblems and storing the solutions to those subproblems to avoid redundant computations. Since LCS problems have optimal substructure (the solution to the problem can be constructed from solutions to its subproblems) and overlapping subproblems (the same subproblem is solved multiple times), dynamic programming is a suitable approach.

# Creating the DP Table: We create a 2D table dp to store the lengths of common subsequences. The rows represent characters of text1, and the columns represent characters of text2. The cell dp[i][j] stores the length of the LCS for the substrings text1[:i] and text2[:j].

# Initializing the DP Table: We initialize the first row and column of the DP table to 0 because if one of the strings is empty, the LCS length is 0.

# Filling the DP Table: We iterate through each character of text1 and text2 and fill the DP table based on the following rules:

# If the characters at the current positions match, we increment the length of the LCS by 1 (adding 1 to the length of the LCS for the substrings without the current characters).
# If the characters don't match, we take the maximum of the lengths of the LCSs obtained by excluding either of the current characters.
# Returning the Result: Once we've filled the entire DP table, the value at dp[m][n] (where m and n are the lengths of text1 and text2, respectively) represents the length of the LCS for the entire strings text1 and text2.

# Time and Space Complexity: The time complexity of this approach is O(m * n), where m and n are the lengths of text1 and text2, respectively. The space complexity is also O(m * n) to store the DP table.

# By following these steps and applying the principles of dynamic programming, we can efficiently find the length of the longest common subsequence between two strings.


class Solution:

  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # Get the lengths of the input strings
    m, n = len(text1), len(text2)

    # Initialize a 2D array to store the lengths of the common subsequences
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table bottom-up
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        # If characters match, add 1 to the length of the previous common subsequence
        if text1[i - 1] == text2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1] + 1
        # If characters don't match, take the maximum length of the previous common subsequences
        else:
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the length of the longest common subsequence
    return dp[m][n]
