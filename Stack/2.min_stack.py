# https://leetcode.com/problems/min-stack/


class MinStack(object):

  def __init__(self):
    #  create another stack call min_stack to keep track of min number
    # min_stack : the min value is always on the top of stack
    self.minStack = []
    self.stack = []

  def push(self, val):
    # append function
    # fruits = ["apple", "banana", "cherry"]
    # fruits.append("orange")
    # ['apple', 'banana', 'cherry', 'orange']

    self.stack.append(val)
    # compare with last value in min_stack if it smaller then append that value to the min_stack
    if not self.minStack or val <= self.minStack[-1]:
      self.minStack.append(val)

# pop() removes the element on the top of the stack.

  def pop(self):
    if self.stack:
      # keep track of min_stack by :
      # check if the value remove is the current min value, then remove the last value(min value) in min_stack
      if self.stack[-1] == self.minStack[-1]:
        self.minStack.pop()
      # remove top element of stack
      self.stack.pop()

# gets the top element of the stack.

  def top(self):
    if self.stack:
      return self.stack[-1]
    return None

  def getMin(self):
    if self.minStack:
      return self.minStack[-1]
    return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
