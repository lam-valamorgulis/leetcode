# https://leetcode.com/problems/ones-and-zeroes/


class Solution:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
      memo = {}

      def sub(index, n_ones, n_zeros):
          # If the subproblem has already been solved, return the memoized result
          if (index, n_ones, n_zeros) in memo:
              return memo[(index, n_ones, n_zeros)]

          # Base Cases
          if index == len(strs) or (n_zeros == 0 and n_ones == 0):
              return 0

          # Calculate the number of ones and zeros in the current string
          ones = strs[index].count('1')
          zeros = len(strs[index]) - ones

          # If the current string cannot be included, move to the next string
          if ones > n_ones or zeros > n_zeros:
              memo[(index, n_ones, n_zeros)] = sub(index + 1, n_ones, n_zeros)
              return memo[(index, n_ones, n_zeros)]

          # Calculate the maximum subset size by either including or excluding the current string
          include = 1 + sub(index + 1, n_ones - ones, n_zeros - zeros)
          exclude = sub(index + 1, n_ones, n_zeros)

          # Update the memoization table with the result
          memo[(index, n_ones, n_zeros)] = max(include, exclude)
          return memo[(index, n_ones, n_zeros)]

      return sub(0, n, m)
