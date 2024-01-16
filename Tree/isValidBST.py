# https://leetcode.com/problems/validate-binary-search-tree/

# how to solve :
# Using inorder_traversal: In-order traversal is a depth-first traversal method that visits the nodes of a tree in the following order:
# Traverse the left subtree.
# Visit the current node.
# Traverse the right subtree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

  def isValidBST(self, root):
    # a recursive to tranversal each node in to order in list
    def inorder_traversal(node, res):
      if node:
        inorder_traversal(node.left, res)
        res.append(node.val)
        inorder_traversal(node.right, res)

    res = []
    inorder_traversal(root, res)

    for i in range(1, len(res)):
      if res[i] <= res[i - 1]:
        return False
    return True
