class Solution(object):

  def groupAnagrams(self, strs):
    hashTable = {}
    listAnagrams = []
    for char in strs:
      sortedChar = ''.join(sorted(char))
      if sortedChar not in hashTable:
        hashTable[sortedChar] = [char]
      else:
        hashTable[sortedChar].append(char)
    for key in hashTable:
      listAnagrams.append(hashTable[key])
    return listAnagrams


sol = Solution()
testA = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(testA)
testB = sol.groupAnagrams([""])
print(testB)
testC = sol.groupAnagrams(["a"])
print(testC)
