# https://leetcode.com/problems/valid-anagram/

class Solution():

  # soluttion 1 :
  # using sorting algorithm, sorted built-in function python will create a arr or char of string, it depend on sorted algorithm the produced a time complexity
  # def isAnagram(self, s, t):
  #   canonical1 = ''.join(sorted(s))
  #   canonical2 = ''.join(sorted(t))
  #   # print(sorted(s))
  #   if canonical2 == canonical1:
  #     return True
  #   return False

  # solution 2 : using hashmap table (key-value dict in python) :
  # step 1: create 2 new hash table to store unique key-value
  # step 2: check if 2 hashtable is equal
  def isAnagram(self, s, t):
    hashTableS, hashTableT = {}, {}
    if len(s) != len(t):
      return False

    for i in range(len(s)):
      # if s[i] not in hashTableS and t[i] not in hashTableT:
      if s[i] not in hashTableS:
        hashTableS[s[i]] = 0
        # hashTableT[t[i]] = 0
      else:
        hashTableS[s[i]] = hashTableS[s[i]] + 1
        # hashTableT[t[i]] = hashTableT[t[i]] + 1

    for j in range(len(t)):
      # if s[i] not in hashTableS and t[i] not in hashTableT:
      if t[j] not in hashTableT:
        hashTableT[t[j]] = 0
        # hashTableT[t[i]] = 0
      else:
        hashTableT[t[j]] = hashTableT[t[j]] + 1
        # hashTableT[t[i]] = hashTableT[t[i]] + 1

    for c in hashTableS:
      if c not in hashTableT:
        return False
      elif hashTableS[c] != hashTableT[c]:
        return False
    return True


sol = Solution()
result = sol.isAnagram('anagram', 'nagaram')
print(result)
result1 = sol.isAnagram('rat', 'car')
print(result1)

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
