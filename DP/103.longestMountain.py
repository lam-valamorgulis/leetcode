# https://leetcode.com/problems/longest-mountain-in-array/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:

    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        longest_mountain = 0
        i = 1

        while i < n - 1:
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Count left slope
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Count right slope
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Update longest mountain
                longest_mountain = max(longest_mountain, right - left + 1)

                # Move i to the end of the right slope
                i = right
            else:
                i += 1

        return longest_mountain
