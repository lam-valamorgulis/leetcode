# https://leetcode.com/problems/decode-ways/submissions/1175707262/

# Identifying Overlapping Subproblems:
# In this problem, the number of ways to decode a string depends on the number of ways to decode its substrings. For instance, to decode the string "226", we need to know the number of ways to decode "22" and "6", which in turn depends on the number of ways to decode "2" and the empty string.
# Formulating the Recurrence Relation:
# We can define a dynamic programming array dp, where dp[i] represents the number of ways to decode the substring ending at index i of the input string.
# To compute dp[i], we consider two cases:
# If the current character s[i] is '0', it cannot be decoded on its own. We check if it can be combined with the previous character s[i-1] to form a valid two-digit code. If so, dp[i] is updated based on dp[i-2], as s[i] and s[i-1] together form a valid code. Otherwise, if '0' cannot be part of a valid two-digit code, dp[i] is set to 0.
# If the current character s[i] is not '0', it can be decoded on its own. We update dp[i] based on dp[i-1]. Additionally, if the previous character s[i-1] and the current character s[i] form a valid two-digit code, we update dp[i] based on dp[i-2].
# Base Cases:
# We initialize dp[0] = 1, as there's only one way to decode an empty string.
# If the first character of the input string is '0', it cannot be decoded, so dp[1] is set to 0. Otherwise, dp[1] is initialized to 1.
# Building the DP Table Bottom-Up:
# We iterate through the characters of the input string from index 1 to n, updating dp[i] based on the recurrence relation described above.
# Returning the Final Result:
# Finally, we return dp[n], where n is the length of the input string, representing the number of ways to decode the entire string.


class Solution:

  def numDecodings(self, s: str) -> int:
    n = len(s)
    if n == 0 or s[0] == '0':
      return 0

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
      # Check if the current character is '0'
      if s[i - 1] == '0':
        # If '0' cannot be part of a valid two-digit code, return 0
        if s[i - 2] != '1' and s[i - 2] != '2':
          return 0
        # Otherwise, update dp[i] based on dp[i-2]
        dp[i] = dp[i - 2] if i > 1 else 1
      else:
        # If the current character is not '0', update dp[i] based on dp[i-1]
        dp[i] = dp[i - 1]
        # If the previous character and the current character form a valid two-digit code, update dp[i] based on dp[i-2]
        if i > 1 and '10' <= s[i - 2:i] <= '26':
          dp[i] += dp[i - 2]

    return dp[n]
