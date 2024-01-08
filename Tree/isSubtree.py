# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# how to solve :
# 0(n*m) : while traversing down each node of root, check node is same tree with subTree


# Definition for a binary tree node.
class TreeNode(object):

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):

  def isSubtree(self, root, subRoot):
    # Helper function to check if two trees are identical
    def isSameTree(p, q):
      if not p and not q:
        return True
      if not p or not q:
        return False
      return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(
          p.right, q.right)

    # Base case: If the current node of the main tree is None, it cannot contain the subtree
    if not root:
      return False

    # Check if the current subtree rooted at 'root' is identical to 'subRoot'
    if isSameTree(root, subRoot):
      return True

    # Recursively check in the left and right subtrees
    return self.isSubtree(root.left, subRoot) or self.isSubtree(
        root.right, subRoot)
