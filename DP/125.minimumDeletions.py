# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0  # Tracks the number of 'b's encountered
        deletions = 0  # Tracks the minimum deletions needed to balance the string
        
        for char in s:
            if char == 'b':
                b_count += 1  # Increment the count of 'b's seen
            elif char == 'a':
                # For each 'a', we can either delete the 'a' or a preceding 'b'
                deletions = min(deletions + 1, b_count)  # Choose the smaller option
        
        return deletions

        