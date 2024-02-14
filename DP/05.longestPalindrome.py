# https://leetcode.com/problems/longest-palindromic-substring/submissions/1175239638/

# Subproblem Identification: Identify subproblems that can be solved independently to build up to the solution of the larger problem. In this case, the subproblem is finding the longest palindrome substring centered at each character or between each pair of adjacent characters.
# Memoization: Store the results of subproblems in a table or array so that they can be reused when needed. In this approach, there's no explicit memoization table because the solution is calculated bottom-up as we expand around each character or pair of characters. However, the longest palindrome found so far (longest) serves as a form of memoization.
# Optimal Substructure: The optimal solution to the larger problem can be constructed from the optimal solutions of its subproblems. Here, the optimal solution to finding the longest palindrome substring in the entire string can be built from the optimal solutions of finding palindromes around each character or each pair of adjacent characters.
# Dynamic Programming Iteration: Iterate through the subproblems, solving each one and updating the solution as needed. In this case, the iteration is done by expanding around each character or each pair of adjacent characters and updating the longest palindrome found so far (longest) accordingly.


class Solution(object):

  def longestPalindrome(self, s):
    # Get the length of the input string
    n = len(s)
    # If the string is empty, return an empty string
    if n == 0:
      return ""

    # Helper function to expand around a center and find the longest palindrome
    def expand(l, r):
      # Expand around the center l and r, checking if characters are equal
      while l >= 0 and r < n and s[l] == s[r]:
        # Move the left pointer to the left
        l -= 1
        # Move the right pointer to the right
        r += 1
      # Return the palindrome substring found
      return s[l + 1:r]

    # Initialize a variable to store the longest palindrome found
    longest = ''

    # Iterate through each character in the string
    for i in range(n):
      # Expand around a single character to find palindromes
      palindrome1 = expand(i, i)
      # Update the longest palindrome if palindrome1 is longer
      if len(palindrome1) > len(longest):
        longest = palindrome1

      # Expand around two adjacent characters to find palindromes
      palindrome2 = expand(i, i + 1)
      # Update the longest palindrome if palindrome2 is longer
      if len(palindrome2) > len(longest):
        longest = palindrome2

    # Return the longest palindrome found
    return longest
