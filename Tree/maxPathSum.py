# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Overall:
# same like find diamiater or tree
# problem :
# + how to keep track the max value
# + how to find the max of tree


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def maxPathSum(self, root):
    """
        :type root: TreeNode
        :rtype: int
        """
    # Initialize a class attribute to store the maximum path sum
    self.max_sum = -float('inf')

    def maxPathSumHelper(node):
      if not node:
        return 0

      # Recursively calculate the maximum path sum for the left subtree
      leftMax = max(0, maxPathSumHelper(node.left))

      # Recursively calculate the maximum path sum for the right subtree
      rightMax = max(0, maxPathSumHelper(node.right))

      # Calculate the current path sum including the current node
      currSum = leftMax + node.val + rightMax

      # Update the overall maximum path sum
      self.max_sum = max(self.max_sum, currSum)

      # Return the maximum path sum for the current subtree rooted at the current node
      return node.val + max(leftMax, rightMax)

    # Start the recursive helper function from the root of the tree
    maxPathSumHelper(root)

    # Return the maximum path sum found
    return self.max_sum
