# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for num in nums:
            if num == ops % 2:
                ops += 1
        return ops
