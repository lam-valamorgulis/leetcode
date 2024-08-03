# https://leetcode.com/problems/optimal-division/


class Solution:

    def optimalDivision(self, nums: List[int]) -> str:
        # If there's only one number, just return it as a string.
        if len(nums) == 1:
            return str(nums[0])

        # If there are two numbers, just return them divided.
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])

        # Convert the first number to a string
        first_number = str(nums[0])

        # Convert the remaining numbers to strings and join them with '/'
        remaining_numbers = "/".join(map(str, nums[1:]))

        # Combine the first number with the joined remaining numbers wrapped in parentheses
        result = first_number + "/(" + remaining_numbers + ")"

        return result
