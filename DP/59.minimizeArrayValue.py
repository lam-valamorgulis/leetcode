# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/


class Solution:

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int,
                           secondLen: int) -> int:
        n = len(nums)

        # Calculate prefix sums for efficient subarray sum calculation
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        # Helper function to get sum of subarray
        def getSum(i, j):
            return prefix_sum[j] - prefix_sum[i]

        # Initialize DP arrays
        dp_first = [0] * (
            n + 1)  # Max sum of firstLen subarray ending at or before i
        dp_second = [0] * (
            n + 1)  # Max sum of secondLen subarray ending at or before i

        # Fill DP arrays
        for i in range(firstLen, n + 1):
            dp_first[i] = max(dp_first[i - 1], getSum(i - firstLen, i))

        for i in range(secondLen, n + 1):
            dp_second[i] = max(dp_second[i - 1], getSum(i - secondLen, i))

        # Find the maximum sum of non-overlapping subarrays
        max_sum = 0

        # Case 1: firstLen subarray comes first
        for i in range(firstLen, n - secondLen + 1):
            max_sum = max(max_sum, dp_first[i] + getSum(i, i + secondLen))

        # Case 2: secondLen subarray comes first
        for i in range(secondLen, n - firstLen + 1):
            max_sum = max(max_sum, dp_second[i] + getSum(i, i + firstLen))

        return max_sum
