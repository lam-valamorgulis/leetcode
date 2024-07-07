# https://leetcode.com/problems/rotate-function/


class Solution:

    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        F = 0

        # Compute F(0)
        for i in range(n):
            F += i * nums[i]

        max_value = F

        # Compute F(k) for k = 1 to n-1
        for k in range(1, n):
            F = F + sum_nums - n * nums[-k]
            max_value = max(max_value, F)

        return max_value
