# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
  # key solution:
  # n = 3 will have a 3 close and 3 open
  # counting the open and close 
  # how to make sure it a well-formed parentheses ?:
  # s = "": when open still < n add "(" and close < open add ")" => that is the only way to create valid well-parentheses

  # code it up:
  # base case : when len s = n x 2
  # a recursive funtion :
  # call itself to create a possible value
  # create a logic to update value to reach the base case to stop the recursive function
  # + open < n : 
  # + close < open

  def generateParenthesis(self, n):
      res = []
      def backtrack(s,open,close):
          # base case : len(s) = n*2 , add to result 
          if n*2 == len(s):
              res.append(s)
              return 
          # if open < n : call a recursive backtrack function to add a "(" to the string
          if open < n:
              backtrack(s+"(", open + 1, close)
          if close < open :
              backtrack(s+")", open, close + 1)

      backtrack("",0,0)
      return res

solution = Solution()
result = solution.generateParenthesis(2)
print(result)