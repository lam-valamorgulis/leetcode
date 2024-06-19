# https://leetcode.com/submissions/detail/1293283171/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0  # Initialize the count of arithmetic slices
        dp = [0] * n  # Dynamic programming array to store the count of slices ending at each index

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                # If the current difference is the same as the previous difference
                dp[i] = dp[i - 1] + 1
                count += dp[i]  # Add the count of slices ending at index i to the total count

        return count
