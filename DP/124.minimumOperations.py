# https://leetcode.com/problems/sorting-three-groups/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
    
        # dp[i] represents the length of the longest non-decreasing subsequence
        # ending at index i
        dp = [1] * n
        
        # Find the longest non-decreasing subsequence
        for i in range(1, n):
            # For each previous element up to current index
            for j in range(i):
                # If current element is >= previous element
                # we can extend the subsequence
                if nums[i] >= nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The minimum operations needed is the total length minus
        # the length of longest non-decreasing subsequence
        return n - max(dp)

        