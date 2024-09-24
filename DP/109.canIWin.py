#https://leetcode.com/problems/can-i-win/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the desiredTotal is 0, the first player automatically wins
        if desiredTotal <= 0:
            return True

        # If the sum of all integers from 1 to maxChoosableInteger is less than desiredTotal,
        # no player can reach the target, hence the first player cannot win
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False

        # Memoization dictionary to store previously computed states
        memo = {}

        # Helper function to recursively check if the current player can win
        def can_player_win(used_numbers, current_total):
            # Convert the used_numbers tuple to a key for memoization
            used_numbers_key = tuple(used_numbers)

            # If we have already computed this state, return the stored result
            if used_numbers_key in memo:
                return memo[used_numbers_key]

            # Try picking any number that hasn't been used yet
            for i in range(1, maxChoosableInteger + 1):
                if not used_numbers[i]:
                    # Mark the number as used
                    used_numbers[i] = True

                    # Check if picking this number leads to a win (current_total + i >= desiredTotal)
                    # or if it forces the other player into a losing state
                    if current_total + i >= desiredTotal or not can_player_win(used_numbers, current_total + i):
                        # Restore the used number and memoize the result
                        used_numbers[i] = False
                        memo[used_numbers_key] = True
                        return True

                    # Restore the used number for future recursive calls
                    used_numbers[i] = False

            # If no winning move was found, store the result and return False
            memo[used_numbers_key] = False
            return False

        # Array to keep track of which numbers have been used
        used_numbers = [False] * (maxChoosableInteger + 1)

        # Call the helper function starting with no numbers used and a current total of 0
        return can_player_win(used_numbers, 0)
