# https://leetcode.com/problems/predict-the-winner/

 class Solution:
     def predictTheWinner(self, nums: List[int]) -> bool:
         memo = {}
         def maxDiff(i, j):
             if (i, j) in memo:
                 return memo[(i, j)]

             if i == j:
                 return nums[i]

             pick_i = nums[i] - maxDiff(i + 1, j)
             pick_j = nums[j] - maxDiff(i, j - 1)
             memo[(i, j)] = max(pick_i, pick_j)

             return memo[(i, j)]

         return maxDiff(0, len(nums) - 1) >= 0

