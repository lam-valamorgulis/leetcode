# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        max_len = 0
        for num in nums:
            for j in range(k):
                remainder = num % k
                dp[remainder][j] = max(dp[remainder][j], dp[j][remainder] + 1)
                max_len = max(max_len, dp[remainder][j])
        return max_len
