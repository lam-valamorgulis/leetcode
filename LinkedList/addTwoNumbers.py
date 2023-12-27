# https://leetcode.com/problems/add-two-numbers/
# Key word :
# remainder 19/10 = 9


# Definition for a Node.
class Node:

  def __init__(self, x, next=None):
    self.val = int(x)
    self.next = next


class Solution(object):

  def addTwoNumbers(self, l1, l2):

    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [7,0,8]
    # Explanation: 342 + 465 = 807.
    # create a dummy NodeList

    dummy_list = Node(0)
    curr = dummy_list
    carry = 0

    while l1 or l2 or carry:
      x = l1.val if l1 else 0
      y = l2.val if l2 else 0
      sum = x + y + carry
      # 19 / 10 = 1.9 => 1
      carry = sum // 10
      # So, 19 % 10 is equal to 9
      # because when you divide 19 by 10, you get 1 with a remainder of 9.
      curr.next = Node((sum % 10))
      curr = curr.next
      if l1:
        l1 = l1.next
      if l2:
        l2 = l2.next
    return dummy_list.next


# solution = Solution()
