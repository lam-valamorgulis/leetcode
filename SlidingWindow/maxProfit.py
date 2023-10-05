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

# class Solution():

#   def lengthOfLongestSubstring(self, s):
#     l, r = 0 , 1
#     sub = ''
#     max = 0
#     while r < len(s):
#       if s[r] not in sub :
#         sub = sub + s[l]
#       else:
#         l = r
#         max = len(sub)
#       print(sub)
#       r +=1
#     return max

# solution = Solution()
# result = solution.lengthOfLongestSubstring("pwwkew")
# print(result)
