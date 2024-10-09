# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)  # Sort in descending order for optimization
        
        # Early exit if the largest number is greater than the target
        if nums[0] > target:
            return False
        
        used = [False] * len(nums)
        memo = {}

        def backtrack(k, current_sum, start):
            # If all k subsets are filled
            if k == 0:
                return True
            # If current subset sum equals target, start a new subset
            if current_sum == target:
                return backtrack(k - 1, 0, 0)
            # Check memoization state
            state = (k, current_sum, tuple(used))
            if state in memo:
                return memo[state]
            
            for i in range(start, len(nums)):
                # Skip used elements or if current sum exceeds target
                if used[i] or current_sum + nums[i] > target:
                    continue
                
                used[i] = True  # Mark the number as used
                if backtrack(k, current_sum + nums[i], i + 1):
                    memo[state] = True
                    return True
                used[i] = False  # Backtrack

            memo[state] = False
            return False

        return backtrack(k, 0, 0)

