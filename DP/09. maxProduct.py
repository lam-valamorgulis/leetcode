# https://leetcode.com/problems/maximum-product-subarray/description/


class Solution:

  def maxProduct(self, nums: List[int]) -> int:
    # Initialize variables to keep track of the maximum and minimum products ending at the current index
    max_product = min_product = result = nums[0]

    # Iterate through the array, starting from the second element
    for num in nums[1:]:
      # Update max_product and min_product
      if num < 0:
        max_product, min_product = min_product, max_product

      max_product = max(num, max_product * num)
      min_product = min(num, min_product * num)

      # Update the result with the maximum value between the current result and max_product
      result = max(result, max_product)

    return result
