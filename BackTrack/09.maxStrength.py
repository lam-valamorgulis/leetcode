# https://leetcode.com/problems/maximum-strength-of-a-group/
class Solution:
  def maxStrength(self, nums: List[int]) -> int:
      def backtrack(index, current_product, is_non_empty):
          nonlocal max_product
          if index == len(nums):
              if is_non_empty:  # Ensure at least one element was included
                  max_product = max(max_product, current_product)
              return

          # Include the current number
          backtrack(index + 1, current_product * nums[index], True)
          # Exclude the current number
          backtrack(index + 1, current_product, is_non_empty)

      max_product = float('-inf')  # Initialize to negative infinity
      backtrack(0, 1, False)  # Start with the first index and product of 1
      return max_product
