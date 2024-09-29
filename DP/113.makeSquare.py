# https://leetcode.com/problems/matchsticks-to-square/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        
        # If total length is not divisible by 4, we cannot form a square
        if total_length % 4 != 0:
            return False
        
        side_length = total_length // 4
        n = len(matchsticks)
        
        # Sort matchsticks in descending order for better pruning
        matchsticks.sort(reverse=True)
        
        # Initialize the 4 sides of the square
        sides = [0] * 4
        
        # Helper function for backtracking
        def backtrack(index):
            # If we've placed all matchsticks, check if all sides are equal to side_length
            if index == n:
                return sides[0] == sides[1] == sides[2] == sides[3] == side_length
            
            # Try to place the current matchstick in one of the four sides
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    
                    # Recurse to place the next matchstick
                    if backtrack(index + 1):
                        return True
                    
                    # Backtrack by removing the matchstick from this side
                    sides[i] -= matchsticks[index]
                
                # If this side is 0, no point in trying the rest of the sides
                if sides[i] == 0:
                    break
            
            return False
        
        # Start the backtracking with the first matchstick
        return backtrack(0)

        