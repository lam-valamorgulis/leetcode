# https://leetcode.com/problems/wiggle-subsequence/


class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # Initialize variables for tracking the previous difference and the count of wiggle sequence
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1

        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]

            # Check if there's a valid alternation between positive and negative differences
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff

        return count
