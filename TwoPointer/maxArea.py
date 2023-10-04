class Solution():

  
  def maxArea(self, h):
    l, r, max = 0, len(h) - 1 , 0
    while l < r :
      vertical = min(h[l],h[r])
      temp = vertical * (r - l)
      if temp >= max :
        max = temp 
      if h[l] < h[r] :
        l +=1
      elif h[l] >= h[r]:
        r -=1
    return max
    
   


solution = Solution()
result = solution.maxArea([1,8,6,2,5,4,8,3,7])
print(result)
