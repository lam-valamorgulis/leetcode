class Solution():

  # solution 1 : using build-in python reverse string
  # can solve in O(1) space complexity ?
  # can solve without build-in reverse string python ?

  # def isPalindrome(self, s):
  #   clean_string = ""
  #   for c in s:
  #     if c.isalpha():
  #       clean_string += c.lower()
  #   return clean_string == clean_string[::-1]

  # solution 2 : optimize code:
  # note : check if two pointer excceed out of range of list
  # function same with isalnum :
  # def is_alnum_ascii(char):
  #   ascii_val = ord(char)
  #   return (48 <= ascii_val <= 57) or (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122)


  def isPalindrome(self, s):
    l, r = 0, len(s) - 1
    
    while l <= r:
        while l <= r and not s[l].isalnum():
            l += 1
        while l <= r and not s[r].isalnum():
            r -= 1
        
        if l <= r and s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    
    return True



solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)
