# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:

    def maximumLength(self, nums: List[int]) -> int:
        c = nums[
            0] % 2  # Check the parity (odd/even) of the first number (0 for even, 1 for odd)
        odd = even = both = 0  # Initialize counters for odd, even, and alternating sequences

        for num in nums:  # Loop through each number in the array
            if num % 2 == 0:  # If the number is even
                even += 1  # Increment the even counter
            else:  # If the number is odd
                odd += 1  # Increment the odd counter

            if num % 2 == c:  # Check if the number has the same parity as expected (matches `c`)
                both += 1  # Increment the 'both' counter for alternating sequences
                c = 1 - c  # Toggle `c` to expect the opposite parity in the next number (switch between 0 and 1)

        return max(
            both, even, odd
        )  # Return the largest valid sequence (alternating, all even, or all odd)
