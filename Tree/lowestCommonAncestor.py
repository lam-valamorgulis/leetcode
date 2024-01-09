# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# how to solve :
# To find the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST), you can use the following algorithm. The key property of a BST that we will leverage is that for any given node:

# If both nodes p and q are smaller than the current node's value, then the LCA must be in the left subtree.
# If both nodes p and q are larger than the current node's value, then the LCA must be in the right subtree.
# If one node is smaller and the other is larger, then the current node is the LCA.


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def lowestCommonAncestor(self, root, p, q):
    # Base case: If the root is None or one of the nodes is found, return the root
    if not root or root == p or root == q:
      return root

    # Search in the left subtree
    left_lca = self.lowestCommonAncestor(root.left, p, q)

    # Search in the right subtree
    right_lca = self.lowestCommonAncestor(root.right, p, q)

    # If both nodes are found in different subtrees, the current node is the LCA
    if left_lca and right_lca:
      return root

    # If one node is found, return that node (either left or right LCA)
    return left_lca or right_lca


# Example usage:
# Create a BST
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

# Nodes to find LCA for
p_node = root.left.left  # Node with value 5
q_node = root.left.right  # Node with value 15

# Create an instance of the Solution class
solution = Solution()

# Find the LCA
lca_node = solution.lowestCommonAncestor(root, p_node, q_node)

# Print the value of the LCA node
print("Lowest Common Ancestor:", lca_node.val)
