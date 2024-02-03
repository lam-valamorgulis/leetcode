# https://leetcode.com/problems/combination-sum/


class Solution(object):

  def combinationSum(self, candidates, target):
    res = []  # Initialize an empty list to store the result combinations.

    def dfs(i, cur, total):
      # Base case: If the current total equals the target, add the current combination to the result.
      if total == target:
        res.append(cur[:])
        return

      # Base case: If the current index is out of bounds or the total exceeds the target, return.
      if i >= len(candidates) or total > target:
        return

      # Include the current candidate in the combination and continue exploring with the same candidate.
      cur.append(candidates[i])
      dfs(i, cur, total + candidates[i])

      # Backtrack: Remove the last added candidate to try different combinations.
      cur.pop()

      # Explore with the next candidate (increment the index).
      dfs(i + 1, cur, total)

    # Start the depth-first search with initial values: index=0, current combination=[], current total=0.
    dfs(0, [], 0)

    # Return the final result containing all valid combinations.
    return res
