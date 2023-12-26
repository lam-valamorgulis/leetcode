# https://leetcode.com/problems/copy-list-with-random-pointer/
# Key word :
# the random pointer can point to any node
# 2 pass


# Definition for a Node.
class Node:

  def __init__(self, x, next=None, random=None):
    self.val = int(x)
    self.next = next
    self.random = random


class Solution(object):

  def copyRandomList(self, head):
    if not head:
      return None

    # First pass: create a mapping between original and new nodes
    mapping = {}
    current = head
    while current:
      mapping[current] = Node(current.val)
      current = current.next

    # Second pass: update next and random pointers of new nodes
    current = head
    while current:
      if current.next:
        mapping[current].next = mapping[current.next]
      if current.random:
        mapping[current].random = mapping[current.random]
      current = current.next

    return mapping[head]


# solution = Solution()
