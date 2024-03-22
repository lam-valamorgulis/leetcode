# https://leetcode.com/problems/jump-game-ii/


class Solution:

  def jump(self, nums: List[int]) -> int:
    n = len(nums)
    jumps = 0
    current_jump_end = 0
    farest = 0

    for i in range(n - 1):
      farest = max(farest, i + nums[i])
      if i == current_jump_end:
        jumps += 1
        current_jump_end = farest
    return jumps
