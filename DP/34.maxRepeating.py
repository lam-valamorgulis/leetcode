# https://leetcode.com/problems/maximum-repeating-substring/


class Solution:

    def maxRepeating(self, sequence: str, word: str) -> int:
        len_seq = len(sequence)
        len_word = len(word)

        # Initialize dp array with zeros
        dp = [0] * len_seq

        # Iterate over each position in the sequence
        for i in range(len_seq):
            # Check if the current segment of length `len_word` matches `word`
            if i >= len_word - 1 and sequence[i - len_word + 1:i + 1] == word:
                if i >= len_word:
                    dp[i] = dp[i - len_word] + 1
                else:
                    dp[i] = 1

        # The maximum value in dp array will be our result
        return max(dp)
