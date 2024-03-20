# https://leetcode.com/problems/maximum-subarray/


class Solution:

  def maxSubArray(self, nums: List[int]) -> int:
    if not nums:
      return 0

    max_curr = max_gol = nums[0]

    for num in nums[1:]:
      max_curr = max(num, max_curr + num)
      max_gol = max(max_gol, max_curr)
    return max_gol
