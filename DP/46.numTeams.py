# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:    
        n = len(rating)
        count = 0

        for j in range(n):
            left_less = left_greater = right_less = right_greater = 0

            # Count soldiers on the left of j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            # Count soldiers on the right of j
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                if rating[k] > rating[j]:
                    right_greater += 1

            # Calculate number of valid teams with j as the middle soldier
            count += left_less * right_greater + left_greater * right_less

        return count

