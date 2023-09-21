# revisit heap, heapify data structure
#  bucket sort
# what is heap use for => best for getting max or min element
# review how to make a heap, transform heap to list 

class Solution(object):

    def topKFrequent(self, nums, k):
        hsT = {}  # Dictionary to store frequency of each element
        fT = {}   # Dictionary to store elements with the same frequency
        
        # Count the frequency of each element
        for n in nums:
            hsT[n] = hsT.get(n, 0) + 1
        
        # Populate the frequency table
        for key, value in hsT.items():
            if value not in fT:
                fT[value] = [key]
            else:
                fT[value].append(key)
        
        res = []
        for x in range(len(nums), 0, -1):  # Corrected the range
          if x in fT:
            for i in fT[x]:
              res.append(i)
        return res[:k]


sol = Solution()
testA = sol.topKFrequent([-1,-1,-1,2,2,3], 2)
print(testA)
testB = sol.topKFrequent([1,2], 2)
print(testB)
