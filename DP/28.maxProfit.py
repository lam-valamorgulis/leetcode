
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
  def maxProfit(self, prices: List[int], fee: int) -> int:
      # Create a memoization dictionary to store previously computed results
      memo = {}

      # Define a recursive function to calculate the maximum profit
      def dp(day, has_stock):
          # If the current state has been computed before, return the result from memo
          if (day, has_stock) in memo:
              return memo[(day, has_stock)]

          # If we reach the end of the prices array, return 0
          if day >= len(prices):
              return 0

          # If we have a stock on the current day
          if has_stock:
              # We can either sell the stock or do nothing
              # If we sell, we get prices[day] - fee, and move to the next day without a stock
              # If we do nothing, we keep the stock and move to the next day
              memo[(day, has_stock)] = max(dp(day + 1, False) + prices[day] - fee, dp(day + 1, True))
          else:
              # If we don't have a stock on the current day
              # We can either buy the stock or do nothing
              # If we buy, we lose prices[day] from our balance and move to the next day with a stock
              # If we do nothing, we remain without a stock and move to the next day
              memo[(day, has_stock)] = max(dp(day + 1, True) - prices[day], dp(day + 1, False))

          return memo[(day, has_stock)]

      # Start the recursive function from the first day without a stock
      return dp(0, False)

