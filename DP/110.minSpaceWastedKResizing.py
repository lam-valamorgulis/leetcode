#https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:
    def minSpaceWastedKResizing(self, nums, maxResizes):
        n = len(nums)
        # dp[i] will store the minimum wasted space considering the first i elements
        dp = [0] + [float('inf')] * n

        # We are allowed up to maxResizes resizes
        for resizeCount in range(maxResizes + 1):
            # We start from the end and move towards the start to calculate the wasted space
            for end in range(n - 1, resizeCount - 1, -1):
                currentSum = 0
                currentMax = 0
                # Now, we calculate the space wasted for all subarrays ending at `end`
                for start in range(end, resizeCount - 1, -1):
                    currentSum += nums[start]
                    currentMax = max(currentMax, nums[start])
                    # Update dp[end + 1] with the minimum wasted space
                    dp[end + 1] = min(dp[end + 1], dp[start] + currentMax * (end - start + 1) - currentSum)

        # Return the minimum wasted space when using up to maxResizes
        return dp[-1]
