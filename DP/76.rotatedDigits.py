# https://leetcode.com/problems/rotated-digits/


class Solution:

    def rotatedDigits(self, n: int) -> int:
        # Define the rotation rules in a dictionary
        rotation = {
            '0': '0',
            '1': '1',
            '8': '8',
            '2': '5',
            '5': '2',
            '6': '9',
            '9': '6'
        }

        def isGoodNumber(x):
            original = str(x)
            rotated = []
            for char in original:
                if char not in rotation:
                    return False  # Invalid digit
                rotated.append(rotation[char])
            rotated_number = ''.join(rotated)
            return rotated_number != original  # Must be different after rotation

        count = 0
        for i in range(1, n + 1):
            if isGoodNumber(i):
                count += 1

        return count
