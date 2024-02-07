# https://leetcode.com/problems/word-search/

# Backtracking Approach:

# Understanding the Problem: The problem is to search for a given word in a 2D board of characters, where adjacent cells (horizontally or vertically) can be combined to form the word.

# Understanding the Code Structure: The code is structured as a class named Solution, containing a method exist that takes a board and a word as input. Inside the exist method, there's a nested function dfs which performs depth-first search (DFS) to search for the word in the board.

# Understanding the dfs Function: The dfs function recursively searches for the word in the board, starting from a given position (i, j). It checks if the current cell matches the first character of the word and then explores neighboring cells to find the remaining characters of the word.

# Analyzing the Main Loop: The main loop iterates over each cell of the board and calls the dfs function for each cell. If dfs returns True, indicating that the word is found starting from that cell, the method immediately returns True. Otherwise, it continues searching until all cells are checked.

# Understanding Backtracking: The code temporarily marks visited cells by replacing their values with "#", but it correctly reverts the changes before backtracking. This ensures that the algorithm explores all possible paths without getting stuck in loops.

# Ensuring Correctness: I ensure that the code handles edge cases correctly, such as empty inputs or words that cannot be found in the board. The code seems to handle these cases properly by returning False in such situations.

# Overall, the code seems well-structured and implements a common backtracking algorithm to solve the word search problem efficiently.


class Solution(object):
  # Define a class named Solution
  def exist(self, board, word):
    # Define a method exist within the Solution class, which takes a board and a word as parameters
    def dfs(board, i, j, word):
      # Define a nested function dfs which performs depth-first search, taking the current position (i, j) and the word to search for
      if len(word) == 0:
        # If the length of the word is 0, it means we've found the entire word
        return True
        # Return True to indicate success
      if i < 0 or i >= len(board) or j < 0 or j >= len(
          board[0]) or board[i][j] != word[0]:
        # If the current position (i, j) is out of bounds or the character at (i, j) does not match the first character of the word
        return False
        # Return False to indicate failure

      temp, board[i][j] = board[i][j], "#"
      # Temporarily store the original character of the board at (i, j) in temp, and mark the cell as visited by replacing its value with "#"
      found = dfs(board, i + 1, j, word[1:]) or dfs(
          board, i - 1, j, word[1:]) or dfs(board, i, j + 1, word[1:]) or dfs(
              board, i, j - 1, word[1:])
      # Recursively search for the remaining characters of the word in the neighboring cells
      board[i][j] = temp
      # Restore the original value of the cell at (i, j)
      return found
      # Return the result of the recursive search

    for i in range(len(board)):
      # Iterate over each row of the board
      for j in range(len(board[0])):
        # Iterate over each column of the board
        if dfs(board, i, j, word):
          # If dfs returns True (indicating the word is found), return True immediately
          return True
    return False
    # Return False if the word is not found in any position on the board
