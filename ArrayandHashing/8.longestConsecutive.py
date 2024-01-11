# https://leetcode.com/problems/longest-consecutive-sequence/description/
# instuitive question :
# how to know the consecutive in the array ?
# reduce the val of number by one and check if in the set() if it in the set() it mean it not the lowest streak
# if it is the lowest then start calting the streak from lowest to until no num in set


class Solution():

  # solution for O(nlog) :
  # key :
  # sorting the list
  # keep track the longest_streak by compare curr_streak to the longest_streak
  def longestConsecutive(self, nums):
    nums.sort()
    longest_streak = 1
    curr_streak = 1

    for i in range(1, len(nums)):
      if nums[i] != nums[i - 1]:
        if nums[i] == nums[i - 1] + 1:
          curr_streak += 1
        else:
          longest_streak = max(longest_streak, curr_streak)
          curr_streak = 1
    return max(longest_streak, curr_streak)

  # solution for O(n):
  # create a unique nums
  # key idea :
  # + if the left of num in nums does not have then it is a starting of sequence
  # + keep track the longest_streak by compare curr_streak to the longest_streak
  # + increment the starting of sequence and check if it in unique nums then longest_streak will incremental 1
  # def longestConsecutive(self, nums):
  #   #  create a unique list of nums except duplicate num
  #   unique_nums = set(nums)
  #   longest_streak = 0

  #   for n in unique_nums:
  #     if n - 1 not in unique_nums:
  #       curr_num = n
  #       curr_streak = 1
  #       while curr_num + 1 in unique_nums:
  #         curr_streak += 1
  #         curr_num +=1
  #       longest_streak = max(curr_streak, longest_streak)
  #   return longest_streak


solution = Solution()
result = solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(result)
