# https://leetcode.com/problems/clone-graph/
# Understand the Problem: The first step is to understand the problem statement clearly. In this case, we're given a reference to the first node of a connected undirected graph, and we need to create a deep copy (clone) of the entire graph.
# Identify the Approach: Since the graph is connected and undirected, both depth-first search (DFS) and breadth-first search (BFS) can be used to traverse the graph and clone it. However, DFS is usually more straightforward to implement recursively, which makes it a natural choice for this problem.
# Design the DFS Function: I would start by designing a DFS function that takes a node as input and returns a cloned copy of that node. This function will recursively clone each neighbor of the current node and construct the cloned graph.
# Track Visited Nodes: To prevent infinite recursion in the case of cycles in the graph, we need to keep track of visited nodes. We can use a hash map to store the mapping between original nodes and their corresponding cloned nodes.
# Implement the DFS Function: With the design in mind, I would implement the DFS function recursively. The function will clone the current node, mark it as visited, and recursively clone each of its neighbors.
# Test the Solution: After implementing the DFS function, it's important to test it with various test cases to ensure it correctly clones the graph.
# Time and Space Complexity Analysis: Finally, I would analyze the time and space complexity of the solution to ensure it meets the requirements of the problem and to identify any potential optimizations.


# Definition for a Node.
class Node(object):

  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


class Solution(object):

  def cloneGraph(self, node):

    def dfs(old):
      if old in oldToNew:
        return oldToNew[old]

      clone = Node(old.val)
      oldToNew[old] = clone

      for nei in old.neighbors:
        clone.neighbors.append(dfs(nei))

      return clone

    oldToNew = {}
    return dfs(node) if node else None
