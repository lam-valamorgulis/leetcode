# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/


class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_max = 0
        current_min = 0

        for num in nums:
            current_max = max(current_max + num, num)
            current_min = min(current_min + num, num)

            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

        return max(max_sum, abs(min_sum))
