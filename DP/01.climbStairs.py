# https://leetcode.com/problems/climbing-stairs/

# We define a class Solution with a method climbStairs that takes an integer n as input.
# We start by checking if n is equal to 1 or 2. If it is, we return 1 or 2 respectively, because there's a specific number of ways to climb when there are only 1 or 2 steps.
# If n is greater than 2, we initialize a list dp of size n+1 to store the number of ways to reach each step.
# We populate dp with the number of ways to reach the first two steps (dp[1] and dp[2]).
# Then, we use a loop to calculate the number of ways to reach each step from step 3 to step n. This is done by summing up the number of ways to reach the previous two steps (dp[i-1] and dp[i-2]).
# Finally, we return the number of ways to reach the nth step, which represents the top of the staircase.


class Solution(object):

  def climbStairs(self, n):
    # Check if there is only one step
    if n == 1:
      return 1  # If there is only one step, there is only one way to climb it

    # Check if there are only two steps
    if n == 2:
      return 2  # If there are two steps, there are two ways to climb it: 1 step at a time or 2 steps at a time

    # Initialize an array to store the number of ways to reach each step
    dp = [0] * (n + 1)  # Create a list with (n+1) elements, initialized to 0

    dp[1] = 1  # There's only one way to reach step 1
    dp[2] = 2  # There are two ways to reach step 2: 1 step at a time or 2 steps at a time

    # Calculate the number of ways to reach each step starting from step 3
    for i in range(3, n + 1):
      dp[i] = dp[i - 1] + dp[
          i -
          2]  # The number of ways to reach step i is the sum of ways to reach step (i-1) and (i-2)

    return dp[
        n]  # Return the number of ways to reach the nth step, which is the top of the staircase
