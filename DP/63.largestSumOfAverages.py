# https://leetcode.com/problems/largest-sum-of-averages/

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        memo = {}

        def dp(i, k):
            # Check if the result is already computed and stored in memo
            if (i, k) in memo:
                return memo[(i, k)]

            # Base case: if no partitions left and reached the end of the array
            if k == 0 and i == n:
                return 0

            # Base case: if no partitions left but haven't reached the end, or reached the end but still need partitions
            if k == 0 or i == n:
                return float('-inf')

            # Initialize variables to compute the current maximum score
            current_sum = 0
            max_score = float('-inf')

            # Iterate over possible partitions
            for j in range(i, n):
                current_sum += nums[j]
                current_average = current_sum / (j - i + 1)
                # Recursive call to compute the score for the remaining elements and partitions
                max_score = max(max_score, current_average + dp(j + 1, k - 1))

            # Store the result in memo to avoid redundant calculations
            memo[(i, k)] = max_score
            return max_score

        return dp(0, k)

