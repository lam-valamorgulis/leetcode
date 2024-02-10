# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# We define a class Solution with a method letterCombinations that takes digits as input.
# We start by checking if the input digits is empty. If it is, there are no combinations possible, so we return an empty list.
# We define a dictionary mapping that maps each digit to its corresponding letters on the phone keypad.
# We define a recursive DFS function dfs that generates combinations. It takes two parameters: combination (the current combination being formed) and next_digits (the remaining digits to be processed).
# If the length of the combination equals the length of the input digits, it means we have formed a complete combination, so we append it to the result list res.
# We iterate through the letters corresponding to the first digit in next_digits, appending each letter to the current combination and recursively calling dfs with the updated combination and the remaining digits.
# We initialize an empty list res to store the results.
# We start DFS with an empty initial combination and the input digits.
# Finally, we return the list of generated combinations.


class Solution(object):

  def letterCombinations(self, digits):
    # Check if the input digits string is empty
    if not digits:
      return []  # If empty, return an empty list

    # Define a mapping of digits to corresponding letters
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # Define a recursive DFS function to generate combinations
    def dfs(combination, next_digits):
      # If the length of the combination equals the length of the input digits,
      # it means we have formed a complete combination. Add it to the result.
      if len(combination) == len(digits):
        res.append(combination)
        return

      # Iterate through the letters corresponding to the first digit in next_digits
      for letter in mapping[next_digits[0]]:
        # Recursively call dfs with the updated combination and remaining digits
        dfs(combination + letter, next_digits[1:])

    # Initialize an empty list to store the results
    res = []
    # Start DFS with an empty initial combination and the input digits
    dfs("", digits)

    # Return the list of generated combinations
    return res
