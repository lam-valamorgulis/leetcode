# https://leetcode.com/problems/find-good-days-to-rob-the-bank/


class Solution:

    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))

        nonIncreasing = [0] * n
        nonDecreasing = [0] * n

        # Fill nonIncreasing array
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                nonIncreasing[i] = nonIncreasing[i - 1] + 1

        # Fill nonDecreasing array
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                nonDecreasing[i] = nonDecreasing[i + 1] + 1

        # Find all good days
        good_days = []
        for i in range(time, n - time):
            if nonIncreasing[i] >= time and nonDecreasing[i] >= time:
                good_days.append(i)

        return good_days
