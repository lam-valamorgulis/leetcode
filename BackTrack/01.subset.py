# https://leetcode.com/problems/subsets/

# Overall:
# the base case :
# the decision tree, left : add element, right don't add


class Solution(object):

  def subsets(self, nums):

    res = []
    subset = []

    def dfs(i):
      if i >= len(nums):
        res.append(subset[:])
        return
      # decision to include nums[i]
      subset.append(nums[i])
      dfs(i + 1)

      # decision NOT to include nums[i]
      subset.pop()
      dfs(i + 1)

    dfs(0)
    return res
