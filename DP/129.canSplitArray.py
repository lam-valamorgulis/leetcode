# https://leetcode.com/problems/check-if-it-is-possible-to-split-array/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM&status=TO_DO%2CATTEMPTED

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2: return True 
        n = len(nums)
        for i in range(1, n): 
            if nums[i] + nums[i - 1] >= m: return True 
        
        return False 