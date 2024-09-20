# https://leetcode.com/problems/longest-turbulent-subarray/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        up = [1] * n
        down = [1] * n
        max_length = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = down[i - 1] + 1
            elif arr[i] < arr[i - 1]:
                down[i] = up[i - 1] + 1

            max_length = max(max_length, up[i], down[i])

        return max_length
