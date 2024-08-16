# https://leetcode.com/problems/construct-the-longest-new-string/


class Solution:

    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            ans = 2 * min(x, y)
        else:
            ans = 2 * min(x, y) + 1
        # print(ans)
        ans += z
        # print(ans)
        return ans * 2
