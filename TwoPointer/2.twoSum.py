# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# create a left pointer and right pointer, examinize the logic pointer itself, while moving the pointer


class Solution():

  # this solution wil add more memory
  # def twoSum(self, numbers, target):
  #   table = {}
  #   for i in range(len(numbers)) :
  #     add_up_num = target - numbers[i]
  #     if add_up_num not in table and numbers[i] <= target:
  #       table[numbers[i]] = i
  #     else:
  #       return [table[add_up_num] + 1 , i + 1]

  #  optimize the solition not using extra memory O(1) memory

  def twoSum(self, numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
      sum = numbers[l] + numbers[r]
      if sum > target:
        r -= 1
      if sum < target:
        l += 1
      else:
        return [l + 1, r + 1]
    return []


solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)
