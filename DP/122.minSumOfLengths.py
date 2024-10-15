# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n  # Track min subarray lengths up to each index
        curr_sum = 0
        left = 0
        result = float('inf')
        best_so_far = float('inf')  # Best length of subarray seen so far
        
        for right in range(n):
            curr_sum += arr[right]
            
            # Shrink window if sum exceeds the target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            # If we find a subarray with sum equal to target
            if curr_sum == target:
                current_length = right - left + 1
                
                # If there's a valid subarray before this one, update the result
                if left > 0 and min_len[left - 1] != float('inf'):
                    result = min(result, current_length + min_len[left - 1])
                
                # Update the minimum length for subarrays up to this point
                best_so_far = min(best_so_far, current_length)
            
            # Store the best length so far in min_len array
            min_len[right] = best_so_far
        
        # Return the result if found, otherwise return -1
        return result if result != float('inf') else -1
        