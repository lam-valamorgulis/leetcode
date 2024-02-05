# https://leetcode.com/problems/subsets-ii/

# Backtracking Approach:

# The goal is to generate all unique subsets of the given array nums.
# The backtracking approach is used, where subsets are explored recursively, and duplicates are avoided.
# Backtracking Function (backtrack):

# The backtrack function takes the result list (res), the current subset (subset), the start index (start), and the input array (nums) as parameters.
# It checks if the current subset is already in the result (res). If yes, it returns, avoiding duplicates.
# It appends a copy of the current subset to the result.
# It then explores further possibilities by iterating through the array from the current start index.
# The current element is included in the subset, and the function is recursively called with the updated subset and start index.
# After the recursive call, the last added element is removed (backtracked).
# Initialization and Execution:

# The main function initializes an empty result list (res) and an empty temporary subset (subset).
# The backtracking process is started with the sorted input array (sorted(nums)) to handle duplicates.
# Return Result:

# The final result contains all unique subsets and is returned.


class Solution(object):

  def subsetsWithDup(self, nums):
    # Backtracking function to generate subsets
    def backtrack(res, subset, start, nums):
      # Check if the current subset is already in the result, if yes, return
      if subset in res:
        return

      # Add the current subset to the result
      res.append(subset[:])

      # Explore further possibilities, avoiding duplicates
      for i in range(start, len(nums)):
        # Include the current element in the subset
        subset.append(nums[i])

        # Recursively call the function with the updated subset and start index
        backtrack(res, subset, i + 1, nums)

        # Backtrack by removing the last added element
        subset.pop()

    # Initialize the result list and temporary subset
    res = []
    subset = []

    # Start the backtracking process with the sorted input array to handle duplicates
    backtrack(res, subset, 0, sorted(nums))

    # Return the list of all subsets
    return res
