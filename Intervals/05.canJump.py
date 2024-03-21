# https://leetcode.com/problems/jump-game/


class Solution:

  def canJump(self, nums: List[int]) -> bool:
    n = len(nums)  # Get the length of the array

    max_reachable = 0  # Initialize the farthest index that can be reached

    # Walk through the path
    for i in range(n):
      # Check if the current index exceeds the farthest reachable index
      if i > max_reachable:
        return False  # If we're stuck, we can't go on

      # Update the farthest reachable index
      max_reachable = max(max_reachable, i + nums[i])

      # Check if we reached the end of the path
      if max_reachable >= n - 1:
        return True  # If we made it to the end, we win!

    return False  # If we couldn't reach the end, we lose
