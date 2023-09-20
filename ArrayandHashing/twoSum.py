class Solution():
  # def twoSum(self, nums, target):
  #   for curr in range(len(nums)):
  #     for next in range(curr,len(nums)):
  #       if target - nums[next] == nums[curr] :
  #         return [curr,next]

  def twoSum(self, nums, target):
    table = {}
    for i in range(len(nums)):
      diff = target - nums[i]
      if diff in table:
        return [table[diff], i]
      table[nums[i]] = i


sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)
result1 = sol.twoSum([3, 3], 6)
print(result1)
