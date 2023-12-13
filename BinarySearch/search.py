# https://leetcode.com/problems/binary-search/

# Key solution :
# - array must be sorting
# - observe the position of the target < , > equal the central point


class Solution:

  def search(self, nums, target):
  #  O(n)

  # for index, num in enumerate(nums) :
  #     if target == num :
  #         return index
  # return -1

  # O(log n)
  l,r = 0, len(nums) - 1
  # left cross the right  
  while l <= r : 
      m = (l + r) / 2
      print(m)
      if nums[m] > target :
          r = m - 1
      elif nums[m] < target :
          l = m + 1
      else :
          return m
  return -1 


solution = Solution()
result = solution.search([-1, 0, 3, 5, 9, 12], 9)
print(result)
