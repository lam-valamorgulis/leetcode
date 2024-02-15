# https://leetcode.com/problems/palindromic-substrings/

# Intuition
# The approach is to expand around each character and each pair of adjacent characters to count the palindromic substrings.

# Approach
# We define a helper function `expand` to count the number of palindromic substrings by expanding around a center.
# Then, we iterate through each character in the string and count palindromic substrings by expanding around it.
# Additionally, for each character, we also expand around the pair of adjacent characters to count palindromic substrings of even length.
# We accumulate the counts obtained from each expansion and return the total count as the result.

# Complexity
# Time complexity: O(n^2) - We iterate through each character and expand around it, resulting in a nested loop.
# Space complexity: O(1) - We use only a constant amount of extra space for variables.


class Solution(object):

  def countSubstrings(self, s):
    n = len(s)

    def expand(l, r):
      temp_count = 0
      while l >= 0 and r < n and s[l] == s[r]:
        temp_count += 1  # Increment count for each palindromic substring found
        l -= 1
        r += 1
      return temp_count

    count = 0

    for i in range(n):
      count = count + expand(i, i) + expand(
          i, i + 1
      )  # Expand around each character and each pair of adjacent characters

    return count
