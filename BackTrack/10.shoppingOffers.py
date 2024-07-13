# https://leetcode.com/problems/shopping-offers/
class Solution:

    def shoppingOffers(self, price: List[int], special: List[List[int]],
                       needs: List[int]) -> int:
        # Memoization dictionary to store results of subproblems
        memo = {}

        def can_apply_offer(current_needs, offer):
            # Check if the offer can be applied without exceeding current needs
            for i in range(len(current_needs)):
                if current_needs[i] < offer[i]:
                    return False
            return True

        def apply_offer(current_needs, offer):
            # Apply the offer and return the new needs
            return [
                current_needs[i] - offer[i] for i in range(len(current_needs))
            ]

        def dfs(current_needs):
            # Convert current needs to a tuple so it can be used as a key for memoization
            needs_tuple = tuple(current_needs)

            # If already computed for this combination of needs, return the stored result
            if needs_tuple in memo:
                return memo[needs_tuple]

            # Base case: cost without any special offers (buying items individually)
            total_cost = sum(current_needs[i] * price[i]
                             for i in range(len(current_needs)))

            # Try every special offer
            for offer in special:
                if can_apply_offer(current_needs, offer):
                    new_needs = apply_offer(current_needs, offer)
                    total_cost = min(total_cost, offer[-1] + dfs(new_needs))

            # Memoize the result for the current needs
            memo[needs_tuple] = total_cost
            return total_cost

        return dfs(needs)
