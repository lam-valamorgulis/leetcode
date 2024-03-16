# https://leetcode.com/problems/edit-distance/


class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
      memo = {}
      def dfs(i, j):
          if (i, j) in memo:
              return memo[(i, j)]

          if i == len(word1):
              return len(word2) - j
          if j == len(word2):
              return len(word1) - i

          if word1[i] == word2[j]:
              memo[(i, j)] = dfs(i + 1, j + 1)
          else:
              insert_op = 1 + dfs(i, j + 1)  # Insertion
              delete_op = 1 + dfs(i + 1, j)  # Deletion
              replace_op = 1 + dfs(i + 1, j + 1)  # Replacement
              memo[(i, j)] = min(insert_op, delete_op, replace_op)

          return memo[(i, j)]

      return dfs(0, 0)


