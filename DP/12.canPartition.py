# https://leetcode.com/problems/partition-equal-subset-sum/


def canPartition(nums):
  total_sum = sum(nums)  # Calculate the total sum of the array
  if total_sum % 2 != 0:  # If the total sum is odd, cannot partition into equal subsets
    return False

  target_sum = total_sum // 2  # The target sum for each subset is half of the total sum
  dp = [False] * (target_sum + 1
                  )  # Initialize a boolean array to track possible sums

  dp[0] = True  # Base case: subset sum of 0 is always possible

  for num in nums:  # Loop through each number in the array
    for i in range(target_sum, num - 1,
                   -1):  # Iterate backwards through the possible sums
      dp[i] = dp[i] or dp[i - num]  # Update the dp array

  return dp[
      target_sum]  # Return whether it's possible to achieve the target sum


# Example usage:
nums1 = [1, 5, 11, 5]
print(canPartition(nums1))  # Output: true

nums2 = [1, 2, 3, 5]
print(canPartition(nums2))  # Output: false
