# https://leetcode.com/problems/koko-eating-bananas/

# Key solution :
# try each value of speed then calculate the total with that speed to find the minimum hours
# adjust left and right when the middle value bigger and smaller than assigned value


class Solution:

  def minEatingSpeed(self, piles, h):
    #  solution 1 : brute force

    #   # loop each speed start from 1 to max pile:
    #   for speed in range(1, max(piles) + 1):
    #     # Check if can finish with the current speed
    #     if can_finish_bruteforce(speed, piles, h):
    #         return speed
    #   # If no speed is found, return 0
    #   return 0

    # def can_finish_bruteforce(speed, piles, h):
    #   total_hours_required = 0
    #   for pile in piles:
    #     # Calculate the hours required to eat the current pile at the given speed
    #     hours_for_pile = math.ceil(piles/speed)
    #         # Accumulate the total hours required
    #     total_hours_required += hours_for_pile

    #     # Check if the total hours required is less than or equal to the available hours
    #   return total_hours_required <= h

    # solution 2 : using binary search mlogn

    # Set initial range for possible eating speeds
    left, right = 1, max(piles)
    res = r

    while left < right:
      # Calculate the middle speed
      mid = (right + left) // 2
      totalTime = 0
      for p in piles:
        totalTime += math.ceil(float(p) / k)
      if totalTime <= h:
        res = k
        r = k - 1
      else:
        l = k + 1
    return res


solution = Solution()
result = solution.minEatingSpeed([1, 3, 5, 7], 3)
print(result)
