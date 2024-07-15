# https://leetcode.com/problems/sort-integers-by-the-power-value/


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def get_power(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps

        # Generate the list of tuples (integer, power)
        power_list = [(i, get_power(i)) for i in range(lo, hi + 1)]

        # Custom sort function
        def custom_sort(pair):
            return pair[1], pair[0]

        # Sort the list using the custom sort function
        power_list.sort(key=custom_sort)

        # Return the k-th element in the sorted list
        return power_list[k - 1][0]
