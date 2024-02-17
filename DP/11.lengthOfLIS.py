# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:

  def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)  # Get the length of the input array
    if n == 0:  # If the array is empty, return 0
      return 0

    # Initialize a dynamic programming array where dp[i] represents the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    # Iterate through each element in nums
    for i in range(1, n):
      # Check all previous elements to find the longest increasing subsequence ending at index i
      for j in range(i):
        if nums[i] > nums[
            j]:  # If nums[i] can be appended to the increasing subsequence ending at index j
          dp[i] = max(
              dp[i], dp[j] + 1
          )  # Update dp[i] to be the maximum between its current value and dp[j] + 1

    # Return the maximum value in dp, which represents the length of the longest increasing subsequence
    return max(dp)


# Example usage:
solution = Solution()
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution.lengthOfLIS(nums1))  # Output: 4
nums2 = [0, 1, 0, 3, 2, 3]
print(solution.lengthOfLIS(nums2))  # Output: 4
nums3 = [7, 7, 7, 7, 7, 7, 7]
print(solution.lengthOfLIS(nums3))  # Output: 1
