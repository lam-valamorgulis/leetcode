class Solution(object):
    def checkInclusion(self, s1, s2):
        def is_permutation(str1,str2):
            return sorted(str1) == sorted(str2)
        len1 = len(s1)
        len2 = len(s2)
        for i in range(len2 - len1 + 1):
            window = s2[i:i+len1]
            if is_permutation(s1,window) :
                return True
        return False


        
    
    


solution = Solution()
result = solution.checkInclusion("ab", "eidbaooo")
print(result)
