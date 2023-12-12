# https://leetcode.com/problems/car-fleet/

# Key solution :
# - sorting the list according the position decensding
# - calculate the time reach the target
# - compare 2 time on the stack

# code it up:


class Solution:

  def carFleet(self, target: int, position: List[int],
               speed: List[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)

    # Use a stack to keep track of the time it takes for each car to reach the target
    stack = []

    # Iterate through the sorted list of cars in reverse order
    for p, s in pair:
      # Calculate the time it takes for the current car to reach the target
      time_to_reach_target = (target - p) / s
      print(time_to_reach_target)

      # Add the time to the stack
      stack.append(time_to_reach_target)

      # Check if there are at least two cars in the stack, and the current car takes less or equal time
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        # If the current car takes less or equal time, pop the last element from the stack
        stack.pop()

    # The length of the stack represents the number of car fleets
    return len(stack)


solution = Solution()
result = solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
print(result)
