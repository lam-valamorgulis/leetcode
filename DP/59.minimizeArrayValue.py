# https://leetcode.com/problems/minimize-maximum-of-array/


class Solution:

    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = 0
        max_value = 0

        for i in range(n):
            current_sum += nums[i]
            max_value = max(max_value, (current_sum + i) // (i + 1))

        return max_value
