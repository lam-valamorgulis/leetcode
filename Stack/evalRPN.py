# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Keynot :
#  stack : last in first out : LIFO
# remove 2 element in stack => calculate then append the result back to the stack

class Solution():

  def evalRPN(self, tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b) / a))
        else:
            stack.append(int(c))
    return stack[0]


solution = Solution()
result = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(result)

