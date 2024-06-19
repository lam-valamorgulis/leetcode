# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
  def findLongestChain(self, pairs: List[List[int]]) -> int:
      # Sort pairs based on their second element
      pairs.sort(key=lambda x: x[1])

      # Initialize variables
      current_end = float('-inf')
      max_chain_length = 0

      # Iterate through sorted pairs
      for pair in pairs:
          if pair[0] > current_end:
              # If the pair can follow the current chain, extend the chain
              current_end = pair[1]
              max_chain_length += 1

      return max_chain_length

