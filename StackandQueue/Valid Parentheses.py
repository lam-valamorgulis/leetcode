class Solution(object):

  def isValid(self, s):
    stack = []
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    for i in range(len(s)):
      if s[i] in open_list:
        stack.append(s[i])
      elif s[i] in close_list:
        if s[i - 1] not in stack:
          return False
    return True
