# https://leetcode.com/problems/binary-tree-right-side-view/

# how to solve :
# Using BFS :
# - BFS uses a queue data structure to keep track of the nodes to be processed.
# - The queue follows the First-In-First-Out (FIFO) principle.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

  def rightSideView(self, root):
    if not root:
      return []

    q = [root]
    res = []
    while q:
      level_size = len(q)
      for i in range(level_size):
        node = q.pop(0)
        if i == (level_size - 1):
          res.append(node.val)
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
    return res
