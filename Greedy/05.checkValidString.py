#https://leetcode.com/problems/valid-parenthesis-string/


class Solution:

  def checkValidString(self, s: str) -> bool:
    min_balance = 0
    max_balance = 0

    for char in s:
      if char == '(':
        min_balance += 1
        max_balance += 1
      elif char == ')':
        min_balance = max(0, min_balance - 1)
        max_balance -= 1
      else:  # char == '*'
        min_balance = max(0, min_balance - 1)
        max_balance += 1

      if max_balance < 0:
        return False

    return min_balance == 0
