# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Key solution :
# navigate the target which is it left part or right part


class Solution:

  def search(self, nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
      m = (l + r) // 2
      # check if the element in the target:
      if nums[m] == target:
        return m
      # if the left sorted
      elif nums[l] <= nums[m]:
        # check if target in the left :
        if nums[left] <= target < nums[m]:
          r = m - 1
        else:
          l = m + 1
      #  if in the right:
      else:
        # The left half is not sorted, so the right half must be sorted
        # Check if the target is in the right half
        if nums[m] < target <= nums[r]:
          l = m + 1
        else:
          r = m - 1
    # If the target is not found, return -1
    return -1


solution = Solution()
#  [4,5,6,7,0,1,2] target 3 #return -1
result = solution.search([4, 5, 6, 7, 8, 0, 1, 2], 0)
print(result)
