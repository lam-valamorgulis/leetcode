# https://leetcode.com/problems/longest-string-chain/
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
            # Sort words by length
        words.sort(key=len)

        # Dictionary to store the longest chain ending with the word
        dp = {}
        max_chain_length = 1

        for word in words:
            dp[word] = 1  # Each word is a chain of at least itself
            for i in range(len(word)):
                # Generate the predecessor by removing one character
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)

            max_chain_length = max(max_chain_length, dp[word])

        return max_chain_length
