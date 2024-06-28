# https://leetcode.com/problems/count-numbers-with-unique-digits/


class Solution:

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        # Initialize the count to include numbers with 1 digit
        count = 10

        # Initialize the number of unique digits for the current number of digits
        unique_digits = 9

        # Iterate from 2 to n
        for i in range(2, n + 1):
            # Calculate the number of unique digits for the current number of digits
            unique_digits *= 10 - (i - 1)

            # Add the number of unique digits to the count
            count += unique_digits

        return count
