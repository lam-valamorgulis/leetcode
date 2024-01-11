# https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution(object):

  def characterReplacement(self, s, k):
    l = 0
    max_len = 0
    max_count = 0
    hashTable = {}

    # right pointer moving with for loop
    for r in range(len(s)):
      # keep track the count of number in string in hashTable:
      hashTable[s[r]] = hashTable.get(s[r], 0) + 1
      max_count = max(max_count, hashTable[s[r]])

      # if is invalid window (number if k is < remain char in window)
      if (r - l + 1) - max_count > k:
        hashTable[s[l]] -= 1
        l += 1
      max_len = max(max_len, r - l + 1)
    return max_len


solution = Solution()
result = solution.characterReplacement("AABABBA", 1)
print(result)

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.
