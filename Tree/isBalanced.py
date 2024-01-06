# https://leetcode.com/problems/diameter-of-binary-tree/

# Overall:
#          Understand the Problem:

# The problem asks us to find the diameter of a binary tree, which is the length of the longest path between any two nodes in the tree.
# Define the Diameter:

# In a binary tree, the diameter might pass through the root node or it might not. So, the diameter is the maximum of:
# The diameter of the left subtree.
# The diameter of the right subtree.
# The sum of the depths of the left and right subtrees (passing through the root).
# Depth-First Search (DFS):

# Use a depth-first search (DFS) approach to traverse the binary tree.
# At each node, calculate the depth of the left and right subtrees recursively.
# Update Diameter:

# At each node, calculate the potential diameter passing through that node (sum of depths of left and right subtrees).
# Update the overall diameter if the potential diameter is greater.
# Return Result:

# The final result will be the overall diameter of the binary tree.
# Example:

# Consider a sample binary tree. For each node, calculate the depths of the left and right subtrees. Update the diameter if the potential diameter passing through that node is greater than the current maximum.


# smaller problem :
# how to make a dfs, count the height of bst
# how to calc the diamiter of the bst
# in time dfs traversing the tree will always keep track of diameter
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def diameterOfBinaryTree(self, root):
    self.diameter = 0  # Variable to store the diameter

    def depth(node):
      if not node:
        return 0
      # Recursively calculate the depth of the left and right subtrees
      left_depth = depth(node.left)
      right_depth = depth(node.right)

      # Update the diameter with the sum of depths of left and right subtrees
      self.diameter = max(self.diameter, left_depth + right_depth)

      # Return the depth of the subtree rooted at the current node
      return 1 + max(left_depth, right_depth)

    depth(root)  # Start the depth calculation from the root
    return self.diameter
