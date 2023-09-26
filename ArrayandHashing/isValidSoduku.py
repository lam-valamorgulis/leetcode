# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# How to solve this problem :
# 1. check each row and col : make sure only digit 1-9 without repetition
# 2. check each sub-box 3x3 make sure each box 1-9 without repetition
# break down a smaller problem:
# - check a list if list has a repetitive elements
# - how to create a list with each column
# - how to create a sub-box 3-3


class Solution():

  def isValidSudoku(self, board):
    # a function to check if list contain repetitive num or not
    def isValid(nums):
      # set is a data structure to only keep track a unique number
      unique = set()
      for n in nums:
        if n != '.' and n in unique:
          return False
        unique.add(n)
      return True

    #  check col and row of sodoku if each col or col contain duplicate num
    # check each row
    for i in range(9):
      if not isValid(board[i]):
        return False

    #check each col
    col = []
    for i in range(9):
      for j in range(9):
        col.append(board[j][i])
    if not isValid(board[i]):
      return False

    # check each sub-box 3x3:
    # looop via each sub box:

    # create a sub-box
    for i in range(0, 9, 3):
      for j in range(0, 9, 3):
        sub_box = []
        # populate sub_box:
        for x in range(3):
          for y in range(3):
            sub_box.append(board[i + x][j + y])
        if not isValid(sub_box):
          return False
    return True


solution = Solution()
result = solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                 [".", ".", ".", ".", "8", ".", ".", "7",
                                  "9"]])
print(result)

# def isValid(nums):
#   unique = set()
#   for n in nums:
#     if n != '.' and n in unique:
#       return False
#     unique.add(n)
#   return True

# print(isValid([1, 2, 3, 4, 4]))  # Output: False
