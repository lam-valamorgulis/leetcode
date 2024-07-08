# https://leetcode.com/problems/extra-characters-in-a-string/submissions/1313746151/


class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)

        # dp[i] represents the minimum number of extra characters
        # when considering the substring s[:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Default: treat current character as extra
            dp[i] = dp[i - 1] + 1

            # Check all possible substrings ending at index i
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]
