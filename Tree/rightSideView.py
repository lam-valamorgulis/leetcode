# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# intuitive:
# search left and right
# during search update count value when traversial the good node
# what is good node ? how to check good node while traversial down the tree ?
# good node : the node after must be higher value than max value of node before
# the max value is the value passing along all the way to the down from the top, it will help to check if the current node X value is higher all the node from the root
#  how to update count value : the result of depth first search each node will be 1 and will add up when recursive

# key note:
# create a recursion function :
# that can take some value as a argument => the value will bring from root to node of none
# during the traversial recursion update that value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

  def goodNodes(self, root):

    def dfs(node, maxVal):
      if not node:
        return 0
      res = 1 if node.val >= maxVal else 0
      maxVal = max(node.val, maxVal)
      res += dfs(node.left, maxVal)
      res += dfs(node.right, maxVal)
      return res

    return dfs(root, root.val)
