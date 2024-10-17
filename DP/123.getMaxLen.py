# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
            # pos_len tracks max length of subarray ending at i with positive product
        # neg_len tracks max length of subarray ending at i with negative product
        pos_len = 0
        neg_len = 0
        max_len = 0
        
        for num in nums:
            if num > 0:
                # For positive number, multiply by it retains sign
                pos_len += 1
                # For negative length, add 1 only if there was a previous negative length
                neg_len = neg_len + 1 if neg_len > 0 else 0
                
            elif num < 0:
                # For negative number, positive becomes negative and vice versa
                new_pos_len = neg_len + 1 if neg_len > 0 else 0
                new_neg_len = pos_len + 1
                pos_len = new_pos_len
                neg_len = new_neg_len
                
            else:  # num == 0
                # Reset both lengths as 0 breaks the subarray
                pos_len = 0
                neg_len = 0
            
            max_len = max(max_len, pos_len)
        
        return max_len

        