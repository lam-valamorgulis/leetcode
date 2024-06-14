# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, direction, length):
            if not node:
                return

            # Update the maximum length found
            self.max_length = max(self.max_length, length)

            if direction == 'left':
                # Move to the left and switch direction to right
                dfs(node.left, 'right', length + 1)
                # Start a new path from the right child
                dfs(node.right, 'left', 1)
            else:  # direction == 'right'
                # Move to the right and switch direction to left
                dfs(node.right, 'left', length + 1)
                # Start a new path from the left child
                dfs(node.left, 'right', 1)

        self.max_length = 0

        # Start DFS from the root, exploring both initial directions
        dfs(root, 'left', 0)
        dfs(root, 'right', 0)

        return self.max_length


# Example usage:
# root = TreeNode(1, None, TreeNode(1, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1, None, TreeNode(1))), TreeNode(1)))
# sol = Solution()
# print(sol.longestZigZag(root))  # Output should be 3
