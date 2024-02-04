# https://leetcode.com/problems/permutations/
# Approach: Backtracking:

# The backtracking approach involves systematically exploring different possibilities to find all solutions.
# In this problem, we can use a recursive backtracking algorithm to generate permutations.
# Solution Steps:

# Base Case:

# The base case of the recursion is when the current permutation (sub) is of the same length as the original array (nums). In this case, we append a copy of the current permutation to the result (res).
# Iteration through Numbers:

# We iterate through each number in the original array (nums).
# For each number, we check if it's already in the current permutation (sub). If it is, we skip to the next iteration.
# Include the Current Number:

# If the current number is not in the current permutation, we include it in the permutation (sub).
# Recursive Call:

# We make a recursive call to the backtrack function with the updated permutation (sub).
# Backtrack:

# After the recursive call, we backtrack by removing the last added element from the permutation (sub).
# Initialization and Execution:

# Initialize an empty result list (res) and an empty temporary sublist (sub).
# Start the backtracking process by calling the backtrack function with the result list, temporary sublist, and the original array (nums).
# Return Result:

# Return the final result list containing all permutations.
# Time Complexity:

# The time complexity is O(N!) because, in the worst case, we generate all possible permutations of the array.
# Space Complexity:

# The space complexity is O(N) due to the recursion stack, where N is the length of the input array (nums). The recursion depth is at most N, and each recursive call adds a constant amount of space.


class Solution(object):

  def permute(self, nums):
    # Helper function to perform backtracking
    def backtrack(res, sub, nums):
      # Base case: if the current permutation is complete, append it to the result
      if len(sub) == len(nums):
        res.append(
            sub[:])  # Append a copy of the current permutation to the result
        return

      # Iterate through each number in the original list
      for i in range(len(nums)):
        # Skip if the number is already in the current permutation
        if nums[i] in sub:
          continue

        # Include the current number in the permutation
        sub.append(nums[i])

        # Recursively call the function with the updated permutation
        backtrack(res, sub, nums)

        # Backtrack by removing the last added element
        sub.pop()

    # Initialize result and temporary sublist
    res = []
    sub = []

    # Start the backtracking process
    backtrack(res, sub, nums)

    # Return the list of all permutations
    return res
