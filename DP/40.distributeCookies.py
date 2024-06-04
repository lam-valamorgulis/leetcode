# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        min_unfairness = float('inf')

        def backtrack(index):
            nonlocal min_unfairness
            if index == len(cookies):
                min_unfairness = min(min_unfairness, max(children))
                return

            for i in range(k):
                children[i] += cookies[index]
                if children[i] < min_unfairness:
                    backtrack(index + 1)
                children[i] -= cookies[index]
                if children[i] == 0:
                    break

        cookies.sort(reverse=True)
        backtrack(0)
        return min_unfairness


