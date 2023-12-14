# https://leetcode.com/problems/search-a-2d-matrix/

# Key solution :
# - binary search
# - analyis brute force, another way
# - main : how to find the middle, how to switch l, r

# solution 1 : binary search to locate where target at which row, then binary search in that row
# solution 2 : faltten all the number arr and binary search


class Solution:

  def searchMatrix(self, matrix, target):
    # # solution 1 :
    # ROWS, COlS = len(matrix), len(matrix[0])

    # top, bot = 0, ROWS - 1
    # #  first loop for navigate which col does the
    # while top <= bot:
    #   # 5//2= 2
    #   row = (bot + top) // 2
    #   if target > matrix[row][-1]:
    #     top = row + 1
    #   elif target < matrix[row][0]:
    #     bot = row - 1
    #   else:
    #     break

    # # if first loop cant locate the map
    # if not (top <= bot):
    #   return False

    # # second loop find target
    # l, r = 0, COLS - 1
    # row = (top + bot) // 2

    # while l <= r:
    #   m = (l + r) // 2
    #   if target > matrix[row][m]:
    #     l = m + 1
    #   elif target < matrix[row][m]:
    #     r = m - 1
    #   else:
    #     return True
    # return False

    # solution 2 :
    # Check if the matrix or its first row is empty
    if not matrix or not matrix[0]:
      return False
    rows, cols = len(matrix), len(matrix[0])
    # Initialize the search range indices for binary search
    left, right = 0, rows * cols - 1

    # Perform binary search on the flattened matrix
    while left <= right:
      # Calculate the middle index
      mid = left + (right - left) // 2
      # Get the element at the middle index in the flattened matrix
      # trick nested arr : get the index of arr by get the module
      mid_element = matrix[mid // cols][mid % cols]
      # Check if the middle element is equal to the target
      if mid_element == target:
          return True
      # If the middle element is less than the target, update the left boundary
      elif mid_element < target:
          left = mid + 1
      # If the middle element is greater than the target, update the right boundary
      else:
          right = mid - 1

      # If the target is not found, return False
    return False


solution = Solution()
result = solution.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
print(result)
