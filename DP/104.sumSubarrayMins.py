# https://leetcode.com/problems/sum-of-subarray-minimums/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        stack = []
        left = [
            0
        ] * n  # left[i] is the distance to the previous smaller element
        right = [0] * n  # right[i] is the distance to the next smaller element

        # Calculate left
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # Clear stack for reuse
        stack.clear()

        # Calculate right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        # Calculate sum without using zip
        total_sum = 0
        for i in range(n):
            total_sum += arr[i] * left[i] * right[i]

        return total_sum % MOD
