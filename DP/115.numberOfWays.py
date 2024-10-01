# https://leetcode.com/problems/number-of-ways-to-select-buildings/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
    
        # Arrays to store number of '0's and '1's before and after each index
        count_zeros_before = [0] * n
        count_ones_before = [0] * n
        count_zeros_after = [0] * n
        count_ones_after = [0] * n
        
        # Count zeros and ones before each index
        for i in range(1, n):
            count_zeros_before[i] = count_zeros_before[i - 1] + (1 if s[i - 1] == '0' else 0)
            count_ones_before[i] = count_ones_before[i - 1] + (1 if s[i - 1] == '1' else 0)
        
        # Count zeros and ones after each index
        for i in range(n - 2, -1, -1):
            count_zeros_after[i] = count_zeros_after[i + 1] + (1 if s[i + 1] == '0' else 0)
            count_ones_after[i] = count_ones_after[i + 1] + (1 if s[i + 1] == '1' else 0)
        
        # Now, count valid selections
        valid_selections = 0
        
        for i in range(n):
            if s[i] == '0':
                # Check how many '101' patterns can be formed with '0' at the middle
                valid_selections += count_ones_before[i] * count_ones_after[i]
            else:
                # Check how many '010' patterns can be formed with '1' at the middle
                valid_selections += count_zeros_before[i] * count_zeros_after[i]
        
        return valid_selections

        