# https://leetcode.com/problems/k-concatenation-maximum-sum/
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        # Helper function to calculate maximum subarray sum using Kadane's algorithm
        def kadane(arr):
            max_current = max_global = 0
            for num in arr:
                max_current = max(num, max_current + num)
                max_global = max(max_global, max_current)
            return max_global

        # Calculate the sum of the array
        arr_sum = sum(arr)

        # Case 1: If k == 1, just return the max subarray sum of the original array
        if k == 1:
            return kadane(arr) % MOD

        # Case 2: If the array sum is positive and k > 1
        max_prefix_sum = kadane(arr)  # Maximum subarray sum for a single copy
        max_prefix_suffix_sum = kadane(arr * 2)  # Maximum subarray sum for two concatenated copies

        if arr_sum > 0:
            # Calculate the maximum sum considering multiple concatenations
            return (max_prefix_suffix_sum + (k - 2) * arr_sum) % MOD
        else:
            # If the sum of the array is non-positive, the best possible sum is from at most two concatenations
            return max(max_prefix_sum, max_prefix_suffix_sum) % MOD
