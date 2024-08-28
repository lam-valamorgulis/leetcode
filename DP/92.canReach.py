# https://leetcode.com/problems/jump-game-vii/


class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':  # If the last index is '1', it's impossible to reach
            return False

        queue = deque([0])
        max_reach = 0  # The furthest index we've reached so far

        while queue:
            i = queue.popleft()

            # Start checking from the maximum of the current index + minJump or the last position we checked
            start = max(i + minJump, max_reach + 1)
            for j in range(start, min(i + maxJump + 1, n)):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)

            # Update the furthest position we've checked
            max_reach = i + maxJump

        return False
