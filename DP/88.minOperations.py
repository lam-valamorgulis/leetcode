# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/



class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n % 2 == 1:  # Check if n is odd
                ans += 1
                n //= 2  # Divide by 2 (same as n = n // 2)
                if n % 2 == 1:  # If n is still odd after dividing by 2
                    n += 1  # Adjust by incrementing n
            else:
                n //= 2  # If n is even, just divide by 2
        return ans