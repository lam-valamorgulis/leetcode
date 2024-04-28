# https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class Solution:

  def findNumberOfLIS(self, nums: List[int]) -> int:
    if not nums:
      return 0

    # Initialize the lengths and counts arrays
    lengths = [1] * len(nums)
    counts = [1] * len(nums)

    # Iterate through the elements of nums
    for i in range(1, len(nums)):
      for j in range(i):
        if nums[i] > nums[j]:
          if lengths[j] + 1 > lengths[i]:
            lengths[i] = lengths[j] + 1
            counts[i] = counts[j]
          elif lengths[j] + 1 == lengths[i]:
            counts[i] += counts[j]

    # Find the maximum length of the longest increasing subsequence
    max_length = max(lengths)
    result = 0

    # Iterate through the lengths and counts arrays
    for i in range(len(nums)):
      if lengths[i] == max_length:
        result += counts[i]

    return result
