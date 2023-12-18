# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Key solution :
# usually O(logn) is binary search
#  the linear graph
# finding the middle, the middle value if bigger then the right most 



class Solution:

  def findMin(self, nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if the minimum element is in the left or right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    # The final 'left' value is the index of the minimum element
    return nums[left]


solution = Solution()
# The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# 5,6,7,0,1,2,4
result = solution.findMin([4, 5, 6, 7, 0, 1, 2])
print(result)
