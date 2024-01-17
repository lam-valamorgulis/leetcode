# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Overall:
# - how to make a dfs
# - how to convert a preorder list to tree


# Definition for a binary tree node.
class TreeNode(object):

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Codec:

  def serialize(self, root):
    """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
    res = []

    # Helper function for recursive depth-first traversal
    def dfs(node):
      # If the node is None, append 'N' to represent null node
      if not node:
        res.append('N')
        return
      # Append the value of the current node to the result
      res.append(str(node.val))
      # Recursively call dfs for the left and right subtrees
      dfs(node.left)
      dfs(node.right)

    # Start the depth-first traversal from the root
    dfs(root)

    # Join the list of values into a comma-separated string
    return ','.join(res)

  def deserialize(self, data):
    """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

    # Split the serialized string into a list of values
    vals = data.split(',')

    # Helper function to recursively build the tree
    def buildTree(vals):
      # If the first value is 'N', pop it and return None
      if vals[0] == 'N':
        vals.pop(0)
        return None

      # Create a node with the value of the first element
      root = TreeNode(int(vals[0]))
      # Pop the first element from the list
      vals.pop(0)
      # Recursively build the left and right subtrees
      root.left = buildTree(vals)
      root.right = buildTree(vals)

      return root

    # Start building the tree from the list of values
    return buildTree(vals)
