# https://leetcode.com/problems/binary-tree-level-order-traversal/

# how to solve :
# Using BFS :
# - BFS uses a queue data structure to keep track of the nodes to be processed.
# - The queue follows the First-In-First-Out (FIFO) principle.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

  def level_order_traversal(self, root):
    if not root:
      return []  # If the tree is empty, return an empty list.

    result = []  # Initialize an empty list to store the final result.
    queue = [root]  # Initialize a queue with the root node.

    while queue:
      current_level = [
      ]  # Initialize an empty list for the current level's values.
      level_size = len(queue)  # Get the number of nodes at the current level.

      for _ in range(level_size):
        node = queue.pop(0)  # Dequeue the front node.
        current_level.append(
            node.val)  # Add the node's value to the current level list.

        if node.left:
          queue.append(node.left)  # Enqueue the left child if it exists.
        if node.right:
          queue.append(node.right)  # Enqueue the right child if it exists.

      result.append(
          current_level)  # Add the current level list to the result list.

    return result  # Return the final result.

  # Example usage:
  root = TreeNode(1)
  root.left = TreeNode(2, TreeNode(4), TreeNode(5))
  root.right = TreeNode(3, TreeNode(6), TreeNode(7))

  result = level_order_traversal(root)
  print(result)
