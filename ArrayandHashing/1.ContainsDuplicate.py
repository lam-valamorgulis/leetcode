# https://leetcode.com/problems/contains-duplicate/


class Solution():

  # ========== SOLUTION 1 ===========
  # The time complexity of this solution is O(n^2)
  # def containsDuplicate(self, nums):
  #   for i in range(len(nums)):
  #     for j in range(0, i):
  #       if nums[j] == nums[i]:
  #         return True
  #   return False

  # ========== SOLUTION 3 ===========
  # def containsDuplicate(self, nums):
  #   nums.sort()
  #   for i in range(len(nums) - 1):
  #     if nums[i] == nums[i + 1]:
  #         return True
  #   return False

  # ========== SOLUTION 3 ===========
  def containsDuplicate(self, nums):
    num_count = {}
    for num in nums:
      if num in num_count:
        return True
      num_count[num] = 1

    return False


# 1,2,3,1
solution = Solution()
result = solution.containsDuplicate([1, 2, 3, 4])
result1 = solution.containsDuplicate([1, 2, 3, 1])
print(result)
print(result1)
