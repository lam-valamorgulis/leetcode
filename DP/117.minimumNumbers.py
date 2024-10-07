# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
    
        for n in range(1, 11):  # Try set sizes from 1 to 10
            # Compute the sum of n numbers where each ends in k
            current_sum = n * k
            # If the sum is less than or equal to num and the difference is divisible by 10
            if current_sum <= num and (num - current_sum) % 10 == 0:
                return n
            
        return -1

        