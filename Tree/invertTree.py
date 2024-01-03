# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Overall:
# - 2 parts :find the value return of base case and recursive call (a tiny different from a given function)
# - call stack visualization
# - break a problem into subproblem, return a value


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):

  def maxDepth(self, root):
    if not root:
      return 0
    else:
      maxLeft = self.maxDepth(root.left)
      maxRight = self.maxDepth(root.right)
      return 1 + max(maxLeft, maxRight)
