# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:

    def getLongestSubsequence(self, words: List[str],
                              groups: List[int]) -> List[str]:
        n = len(words)
        if n == 0:
            return []

        # Initialize DP array to store the length of the longest alternating subsequence ending at each index
        dp = [1] * n
        parent = [-1] * n  # To reconstruct the path

        # Fill the dp array
        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

        # Find the index of the maximum value in dp
        max_length = max(dp)
        index = dp.index(max_length)

        # Reconstruct the longest alternating subsequence
        result = []
        while index != -1:
            result.append(words[index])
            index = parent[index]

        # The result list is in reverse order, so we need to reverse it
        result.reverse()
        return result
