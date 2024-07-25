# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

 MOD = 10**9 + 7

 class Solution:
     def numRollsToTarget(self, n: int, k: int, target: int) -> int:
         memo = {}
         def ways(i, t):
             if i == n:
                 return 1 if t == 0 else 0
             if t < 0:
                 return 0
             if (i, t) in memo:
                 return memo[(i, t)]
             result = 0
             for x in range(1, k + 1):
                 result += ways(i + 1, t - x)
                 result %= MOD
             memo[(i, t)] = result
             return result

         return ways(0, target)

