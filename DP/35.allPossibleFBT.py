#https://leetcode.com/problems/all-possible-full-binary-trees/


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # Memoization dictionary to store already computed results
        memo = {}

        # Helper function to generate all full binary trees with `n` nodes
        def generate_trees(n):
            # Check if result for `n` is already computed
            if n in memo:
                return memo[n]

            # Base case: If `n` is 1, return a list with a single node tree
            if n == 1:
                return [TreeNode(0)]

            result = []
            # Iterate through all possible left subtree sizes
            for i in range(1, n,
                           2):  # i ranges from 1 to n-1, step by 2 (only odd)
                # Recursively generate all left subtrees with `i` nodes
                left_trees = generate_trees(i)
                # Recursively generate all right subtrees with `n-1-i` nodes
                right_trees = generate_trees(n - 1 - i)

                # Combine each left subtree with each right subtree
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)  # Create a new root node
                        root.left = left  # Attach left subtree
                        root.right = right  # Attach right subtree
                        result.append(
                            root)  # Add the new tree to the result list

            # Memoize the result for current `n`
            memo[n] = result
            return result

        # Return the result from the helper function
        return generate_trees(n)


# Example usage:
# Function to convert a tree to a list representation for easy visualization
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while any(queue):
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def print_trees(trees):
    all_trees = []
    for root in trees:
        all_trees.append(tree_to_list(root))
    return all_trees


# Test examples
sol = Solution()

trees_7 = sol.allPossibleFBT(7)
print(print_trees(trees_7))  # Output: list of trees in level order for n=7

trees_3 = sol.allPossibleFBT(3)
print(print_trees(trees_3))  # Output: list of trees in level order for n=3
