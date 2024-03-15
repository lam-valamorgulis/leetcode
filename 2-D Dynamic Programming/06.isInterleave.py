# https://leetcode.com/problems/interleaving-string/description/?source=submission-noac


class Solution:

  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
      return False

    def dfs(idx1, idx2, idx3):

      if (idx1, idx2) in cache:
        return cache[(idx1, idx2)]

      if idx3 == len(s3):
        return True

      if idx1 < len(s1) and s1[idx1] == s3[idx3]:
        if dfs(idx1 + 1, idx2, idx3 + 1):
          cache[(idx1, idx2)] = True
          return True

      if idx2 < len(s2) and s2[idx2] == s3[idx3]:
        if dfs(idx1, idx2 + 1, idx3 + 1):
          cache[(idx1, idx2)] = True
          return True

      cache[(idx1, idx2)] = False
      return False

    cache = {}
    return dfs(0, 0, 0)
