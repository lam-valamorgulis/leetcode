# https://leetcode.com/problems/palindrome-partitioning/

# Understanding the Task: The goal of this code is to take a string s and break it down into substrings, such that each substring is a palindrome (a word that reads the same forwards and backwards).

# Approach with Depth-First Search (DFS): The code uses a popular algorithmic technique called Depth-First Search (DFS) to solve the problem. DFS is a way to explore all possibilities systematically.

# Checking for Palindromes: The checkSub() function checks if a given substring is a palindrome. It does this by comparing characters from the start and end of the substring and moving towards the middle. If all characters match, it's a palindrome.

# Recursive Partitioning: The dfs() function recursively partitions the string into palindromic substrings. It starts with the first character of the string and explores all possible partitions.

# Backtracking: If a palindrome substring is found, it's added to the current partition (path). Then, the function recurses to partition the remaining substring. After exploring all possibilities, it "backtracks" by removing the last added substring, allowing the exploration of other possibilities.

# Collecting Results: As the DFS progresses, it collects valid partitions (where the entire string is covered) into the res list.

# Returning the Result: Finally, the res list containing all valid partitions is returned.


class Solution(object):

  def partition(self, s):

    def checkSub(s, l, r):
      while l <= r:
        if s[l] != s[r]:
          return False
        l += 1
        r -= 1
      return True

    def dfs(start):
      if start == len(s):
        res.append(
            path[:]
        )  # Append a copy of 'path' to 'res' since 'path' will change
        return

      for end in range(start, len(s)):
        if checkSub(s, start, end):
          path.append(s[start:end +
                        1])  # Include the palindrome substring in 'path'
          dfs(end +
              1)  # Recur for the remaining substring after the palindrome
          path.pop()  # Backtrack: remove the last added palindrome substring

    res = []
    path = []
    dfs(0)
    return res
