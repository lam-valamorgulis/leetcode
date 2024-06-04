#https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/

class Solution(object):
    def numSplits(self, s):
        n = len(s)
        left = [0] * n
        right = [0] * n

        distinct_chars = set()
        for i in range(n):
            distinct_chars.add(s[i])
            left[i] = len(distinct_chars)

        distinct_chars = set()
        for i in range(n - 1, -1, -1):
            distinct_chars.add(s[i])
            right[i] = len(distinct_chars)

        num_good_splits = 0
        for i in range(1, n):
            if left[i - 1] == right[i]:
                num_good_splits += 1

        return num_good_splits

