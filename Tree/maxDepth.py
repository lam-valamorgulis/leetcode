# https://leetcode.com/problems/invert-binary-tree/

# Overall:
# - recursive is elegant way to code
# - 2 parts : base case and recursive call (a tiny different from a given function)
# - call stack visualization
# - break a problem into subproblem, return a value

# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def invertTree(self, root):
    if not root:
      return None

    # swap the children
    root.left, root.right = root.right, root.left

    # make 2 recursive calls
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
