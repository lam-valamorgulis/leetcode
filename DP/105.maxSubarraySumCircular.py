# https://leetcode.com/problems/maximum-sum-circular-subarray/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def kadane(arr):
            max_sum = float('-inf')
            current_sum = 0
            for num in arr:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum

        # Case 1: Maximum sum subarray does not wrap around
        max_sum = kadane(nums)

        # Case 2: Maximum sum subarray wraps around
        total_sum = sum(nums)
        inverted_nums = [-num for num in nums]
        wrap_sum = total_sum + kadane(inverted_nums)

        # If all numbers are negative, return the maximum (which is the least negative)
        if wrap_sum == 0:
            return max_sum

        return max(max_sum, wrap_sum)
