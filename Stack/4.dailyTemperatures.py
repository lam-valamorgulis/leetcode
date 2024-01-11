# https://leetcode.com/problems/daily-temperatures/

# Key solution :
# + the future day higher can be count by subtract 2 index

# code it up:
# + how to code O(n):
# We iterate through the temperatures using a for loop.
# We use a stack to store the index of the temperatures.
#  the stack store the index of temperature decreasing
# For each temperature, we check if it is greater than the temperature at the index stored at the top of the stack.
# If yes, we update the result for the corresponding index and continue checking with the next index in the stack.
# We push the current index onto the stack.
# At the end, the result array contains the number of days to wait for a warmer temperature for each day.


class Solution():

  def dailyTemperatures(self, temperatures):
    #  result store a count of future
    #  stack to store a index of temperature : the top of stack will be remove when the next temp will higher than the temp[index top of stack]
    
    n = len(temperatures)
    res = [0] * n
    stack = []

    for i in range(n):
      # tempt at i index is greater than the tempt at top of stack
      while stack and temperatures[i] > temperatures[stack[-1]]:
        prev_index = stack.pop()
        res[prev_index] = i - prev_index
      stack.append(i)
    return res


solution = Solution()
result = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(result)
