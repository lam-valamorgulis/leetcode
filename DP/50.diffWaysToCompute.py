# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(expression, memo):
            if expression in memo:
                return memo[expression]

            results = []
            for i, char in enumerate(expression):
                if char in "+-*":
                    # Split the expression into two parts and solve them recursively
                    left_results = compute(expression[:i], memo)
                    right_results = compute(expression[i+1:], memo)

                    # Combine the results from left and right parts
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)

            # If there are no operators, it's a single number
            if not results:
                results.append(int(expression))

            memo[expression] = results
            return results

        memo = {}
        return compute(expression, memo)

