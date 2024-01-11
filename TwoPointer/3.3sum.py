# https://leetcode.com/problems/3sum/


class Solution():

  # sorted arr + two sum II:
  # nums = [-1, 0, 1, 2, -1, -4]
  def threeSum(self, nums):
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
      # skip duplicate
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      # using two pointer for the rest of arr
      l, r = i + 1, len(nums) - 1
      while l < r:
        sum = nums[l] + nums[r] + nums[i]

        if sum > 0:
          r -= 1
        elif sum < 0:
          l += 1
        else:
          res.append([nums[i], nums[l], nums[r]])
          while l < r and nums[l] == nums[l + 1]:
            l += 1
          while l < r and nums[r] == nums[r - 1]:
            r -= 1
          r -= 1
          l += 1

    return res


solution = Solution()
result = solution.threeSum([0, 0, 0])
print(result)
