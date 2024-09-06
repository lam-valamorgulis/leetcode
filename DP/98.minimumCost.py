
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        h, v = 0, 0  # Number of horizontal and vertical pieces
        total_cost = 0

        while h < len(horizontalCut) and v < len(verticalCut):
            # If the next horizontal cut is more expensive, take it
            if horizontalCut[h] > verticalCut[v]:
                total_cost += horizontalCut[h] * (v + 1)
                h += 1
            # Otherwise, take the vertical cut
            else:
                total_cost += verticalCut[v] * (h + 1)
                v += 1

        # If we have remaining horizontal cuts
        while h < len(horizontalCut):
            total_cost += horizontalCut[h] * (v + 1)
            h += 1

        # If we have remaining vertical cuts
        while v < len(verticalCut):
            total_cost += verticalCut[v] * (h + 1)
            v += 1

        return total_cost
