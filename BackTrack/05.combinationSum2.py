# https://leetcode.com/problems/combination-sum-ii/

# Backtracking Approach:

# Sort the candidates list.
# Define a recursive function to generate combinations.
# Iterate through the candidates, adding each candidate to the current combination.
# Recur with updated parameters:
# Pass the index of the next candidate to be considered to avoid reusing the same candidate.
# Pass the remaining target after subtracting the current candidate.
# When the target becomes zero, add the current combination to the result.
# Backtrack by removing the last added candidate to explore other possibilities.
# Return the result containing unique combinations.


class Solution:

  def combinationSum2(self, candidates, target):

    def backtrack(start, subset, res, candidates, target):
      if target == 0:
        res.append(subset[:])
        return

      for i in range(start, len(candidates)):
        # Avoid duplicates by skipping candidates with the same value
        if i > start and candidates[i] == candidates[i - 1]:
          continue

        # Skip candidates that are greater than the remaining target
        if candidates[i] > target:
          break

        # Add current candidate to the subset
        subset.append(candidates[i])

        # Recur with updated parameters
        backtrack(i + 1, subset, res, candidates, target - candidates[i])

        # Backtrack by removing the last added candidate
        subset.pop()

    res = []
    subset = []
    candidates.sort()  # Sort candidates to easily skip duplicates
    backtrack(0, subset, res, candidates, target)
    return res
