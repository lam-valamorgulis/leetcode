# https://leetcode.com/problems/permutation-in-string/


class Solution(object):
  # def checkInclusion(self, s1, s2):
  #     def is_permutation(str1,str2):
  #         return sorted(str1) == sorted(str2)
  #     len1 = len(s1)
  #     len2 = len(s2)
  #     for i in range(len2 - len1 + 1):
  #         window = s2[i:i+len1]
  #         if is_permutation(s1,window) :
  #             return True
  #     return False
  def checkInclusion(self, s1, s2):

    def char_to_int(c):
      # Map characters to integers (a=0, b=1, ..., z=25)
      return ord(c) - ord('a')

    if len(s1) > len(s2):
      return False

    s1_counter = [0] * 26  # Array to count occurrences of characters in s1
    window_counter = [
        0
    ] * 26  # Array to count occurrences of characters in the window

    for i in range(len(s1)):
      s1_counter[char_to_int(s1[i])] += 1
      window_counter[char_to_int(s2[i])] += 1

    for i in range(len(s2) - len(s1)):
      if window_counter == s1_counter:
        return True

      # Update the window by removing the leftmost character
      window_counter[char_to_int(s2[i])] -= 1
      window_counter[char_to_int(s2[i + len(s1) - 1])] += 1

    # Check the last window
    return window_counter == s1_counter
