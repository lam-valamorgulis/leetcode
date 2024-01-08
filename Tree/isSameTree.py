# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# how to solve :
# using DFS to traversal from root to bottom


class TreeNode(object):

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):

  def isSameTree(self, p, q):
    # Base case: if both nodes are None, they are the same
    if not p and not q:
      return True
    # If one of the nodes is None and the other is not, they are different
    if not p or not q:
      return False
    # Check if the values of the current nodes are equal
    if p.val != q.val:
      return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(
        p.right, q.right)
