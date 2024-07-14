# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/


class Solution:

    def countSubstrings(self, s: str, t: str) -> int:

        s_len = len(s)
        t_len = len(t)
        memo = {}

        def count_diff_by_one(i, j, mismatch):
            # Base cases
            if mismatch > 1:  # More than one mismatch
                return 0
            if i >= s_len or j >= t_len:  # Out of bounds
                return 0

            # Use memoization to save already computed results
            if (i, j, mismatch) in memo:
                return memo[(i, j, mismatch)]

            # Initial result without including current characters
            result = 0

            # If characters differ, increment mismatch
            if s[i] != t[j]:
                mismatch += 1

            # If mismatch is exactly 1, this substring pair is valid
            if mismatch == 1:
                result += 1

            # Recur for next characters in both strings
            result += count_diff_by_one(i + 1, j + 1, mismatch)

            # Save the result in memo and return
            memo[(i, j, mismatch)] = result
            return result

        total_count = 0

        # Iterate over all starting positions in s and t
        for i in range(s_len):
            for j in range(t_len):
                total_count += count_diff_by_one(i, j, 0)

        return total_count
