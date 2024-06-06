# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


class Solution:

  def longestSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(n):
      if nums[right] == 0:
        zero_count += 1

      while zero_count > 1:
        if nums[left] == 0:
          zero_count -= 1
        left += 1

      # Calculate the length of the current window
      # We subtract one because we need to delete one element
      max_len = max(max_len, right - left)

    # The result is the length of the longest subarray of 1's after deleting one element
    return max_len
