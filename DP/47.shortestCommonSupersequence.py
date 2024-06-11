# https://leetcode.com/problems/shortest-common-supersequence/

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        memo = {}

        # Function to find the LCS using memoization
        def lcs(i, j):
            if i == m or j == n:
                return ""
            if (i, j) in memo:
                return memo[(i, j)]
            if str1[i] == str2[j]:
                memo[(i, j)] = str1[i] + lcs(i + 1, j + 1)
            else:
                res1 = lcs(i + 1, j)
                res2 = lcs(i, j + 1)
                memo[(i, j)] = res1 if len(res1) > len(res2) else res2
            return memo[(i, j)]

        # Compute the LCS
        lcs_str = lcs(0, 0)

        # Use the LCS to construct the SCS
        i, j, lcs_idx = 0, 0, 0
        result = []

        for c in lcs_str:
            while i < m and str1[i] != c:
                result.append(str1[i])
                i += 1
            while j < n and str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i += 1
            j += 1

        # Add remaining characters
        result.append(str1[i:])
        result.append(str2[j:])

        return ''.join(result)


