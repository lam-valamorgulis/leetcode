# https://leetcode.com/problems/valid-parentheses/


class Solution(object):

  def isValid(self, s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for c in s:
      if c in bracket_map.values():
        stack.append(c)
      elif stack == [] or bracket_map[c] != stack.pop():
        return False

    return stack == []


obj = Solution()
result = obj.isValid("((({})))")
print(result)
