# https://leetcode.com/problems/redundant-connection/


class Solution(object):

  class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

      def has_cycle(graph, start, visited, parent):
        visited.add(start)
        for neighbor in graph[start]:
          if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, start):
              return True
          elif neighbor != parent:
            return True
        return False

      # Build the graph
      graph = {}
      for edge in edges:
        u, v = edge
        if u not in graph:
          graph[u] = []
        if v not in graph:
          graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

        # Check for cycle
        visited = set()
        if has_cycle(graph, u, visited, None):
          return edge

      return None
