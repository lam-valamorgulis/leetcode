# https://leetcode.com/problems/binary-trees-with-factors/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        
        for i in range(len(arr)):
            dp[arr[i]] = 1  # Each element can be a tree by itself (leaf node)
        
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:  # arr[j] is a potential left child
                    right = arr[i] // arr[j]  # Potential right child
                    if right in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[right]
                        dp[arr[i]] %= MOD
        
        return sum(dp.values()) % MOD

        