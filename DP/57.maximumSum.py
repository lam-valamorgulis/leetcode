# https://leetcode.com/problems/largest-divisible-subset/
class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]

        # Initialize dp arrays
        dp0 = [0] * n
        dp1 = [0] * n

        # Base case
        dp0[0] = arr[0]
        dp1[0] = arr[0]

        # Initialize max_sum with the first element
        max_sum = arr[0]

        # Iterate through the array to fill dp arrays
        for i in range(1, n):
            # Update dp0[i]
            dp0[i] = max(arr[i], dp0[i - 1] + arr[i])

            # Update dp1[i]
            dp1[i] = max(dp0[i - 1], dp1[i - 1] + arr[i])

            # Update the maximum sum found so far
            max_sum = max(max_sum, dp0[i], dp1[i])

        return max_sum
