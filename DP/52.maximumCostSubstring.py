# https://leetcode.com/problems/find-the-substring-with-maximum-cost/


class Solution:

    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # Create a mapping from character to its cost
        char_to_val = {char: vals[i] for i, char in enumerate(chars)}

        # Generate the list of values for the string s
        value_list = []
        for char in s:
            if char in char_to_val:
                value_list.append(char_to_val[char])
            else:
                value_list.append(ord(char) - ord('a') + 1)

        # Use Kadane's Algorithm to find the maximum sum subarray
        max_cost = float('-inf')
        current_cost = 0

        for value in value_list:
            current_cost = max(value, current_cost + value)
            max_cost = max(max_cost, current_cost)

        # The maximum cost of an empty substring is considered 0
        return max(max_cost, 0)
