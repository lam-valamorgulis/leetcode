# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/


class Solution:

    def minimumCost(self, s: str) -> int:
        # Get the length of the string
        length = len(s)

        # Initialize the total cost to 0
        total_cost = 0

        # Iterate through the string, starting from the second character
        for i in range(1, length):
            # Check if the current character is different from the previous one
            if s[i] != s[i - 1]:
                # Calculate the cost for the transition
                transition_cost = min(i, length - i)
                # Add the transition cost to the total cost
                total_cost += transition_cost

        # Return the total cost
        return total_cost
