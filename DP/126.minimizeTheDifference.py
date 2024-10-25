# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM&status=TO_DO%2CATTEMPTED


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        @cache
        def solve(idx, curr_sum):
            if idx == len(mat):
                return abs(target - curr_sum)
            
            min_res = float("inf")
            for x in set(mat[idx]):
                res = solve(idx + 1, curr_sum + x)
                min_res = min(res, min_res)
                if min_res == 0:
                    return 0
            return min_res

        return solve(0, 0)
