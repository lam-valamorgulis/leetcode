# https://leetcode.com/problems/word-break/submissions/1177536045/


class Solution(object):

  def wordBreak(self, s, wordDict):
    n = len(s)

    # Create a set from wordDict for faster lookup
    word_set = set(wordDict)

    # Initialize a dynamic programming array to keep track of whether a substring can be segmented
    dp = [False] * (n + 1)

    # Base case: an empty string can be segmented
    dp[0] = True

    # Iterate through each character in the string
    for i in range(1, n + 1):
      # Iterate through all possible break points before the current character
      for j in range(i):
        # Check if the substring from j to i is in the wordDict and if dp[j] is True
        if dp[j] and s[j:i] in word_set:
          # If so, mark dp[i] as True and break the loop
          dp[i] = True
          break

    # Return dp[n], which indicates whether the entire string can be segmented
    return dp[n]
