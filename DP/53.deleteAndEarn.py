# https://leetcode.com/problems/delete-and-earn/


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Create a frequency map
        max_num = max(nums)
        frequency = [0] * (max_num + 1)
        for num in nums:
            frequency[num] += 1

        # Memoization dictionary
        memo = {}

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return frequency[1]
            if i not in memo:
                take = i * frequency[i] + dp(i - 2)
                skip = dp(i - 1)
                memo[i] = max(take, skip)
            return memo[i]

        return dp(max_num)
