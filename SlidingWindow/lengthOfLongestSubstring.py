class Solution():

  def lengthOfLongestSubstring(self, s):
    l, m = 0, 0
    seen = set()

    for r in range(len(s)):
      curr = s[r]
      # if curr already in hashtable
      if curr in seen:
        # remove char, set() is FIFO
        while s[l] != curr:
          seen.remove(s[l])
          l += 1
        l += 1
      seen.add(s[r])
      m = max(m, r - l + 1)

    return m


solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcbb")
print(result)
# curr = len(sub)
# if curr > max :
#   curr = max
# sub = s[l]
