# https://leetcode.com/problems/number-of-matching-subsequences/submissions/1335984617/


class Solution:

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def is_subsequence(word, s_index):
            if not word:
                return True

            if s_index >= len(s):
                return False

            for i in range(s_index, len(s)):
                if s[i] == word[0]:
                    return is_subsequence(word[1:], i + 1)

            return False

        count = 0
        for word in words:
            if is_subsequence(word, 0):
                count += 1

        return count
