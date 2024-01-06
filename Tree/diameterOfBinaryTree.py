# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# how to solve :
# + for each node calc the diff of depth of node.right and node.left
# +check each every node in sub-tree cant


# This code checks if a binary tree is balanced by calculating the height difference between left and right subtrees for each node. If any subtree is unbalanced, the entire tree is considered unbalanced. If all subtrees are balanced, the overall tree is considered balanced.
class TreeNode(object):

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):

  def isBalanced(self, root):
    # Function to calculate the depth of a subtree rooted at a given node
    def depth(node):
      # Base case: If the node is None (empty), return 0
      if not node:
        return 0

      # Recursively calculate the depth of the left and right subtrees
      left_depth = depth(node.left)
      right_depth = depth(node.right)

      # Check if the subtree is unbalanced
      if left_depth == -1 or right_depth == -1 or abs(left_depth -
                                                      right_depth) > 1:
        return -1  # Indicates that the subtree is unbalanced

      # If the subtree is balanced, return the height of the subtree
      return 1 + max(left_depth, right_depth)

    # Start the depth calculation from the root of the tree
    # If the overall tree is balanced, the result will be the height of the tree
    # If unbalanced, the result will be -1
    return depth(root) != -1
