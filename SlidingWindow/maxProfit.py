class Solution():

  def maxProfit(self, prices):
    l, r = 0, 1
    max = 0
    while r < len(prices):
      if prices[l] >= prices[r]:
        l = r
      else:
        val = prices[r] - prices[l]
        if val > max:
          max = val
      r += 1
    return max


solution = Solution()
result = solution.maxProfit([8, 7, 1, 5, 3, 9, 4])
print(result)
