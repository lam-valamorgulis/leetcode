# https://leetcode.com/problems/counting-bits/


class Solution:

    def countBits(self, n: int) -> List[int]:
        # Create a list to hold our counts
        counts = [0] * (n + 1)

        # Go through each number and count red toys
        for i in range(1, n + 1):
            # If i is even, it has the same number of red toys as i // 2
            counts[i] = counts[i // 2]
            # If i is odd, it has one more red toy than i - 1
            if i % 2 == 1:
                counts[i] = counts[i - 1] + 1

        return counts
