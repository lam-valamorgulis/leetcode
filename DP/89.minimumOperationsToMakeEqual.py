        # https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/


        from collections import deque

        class Solution:
            def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
                # Queue for BFS
                queue = deque([(x, 0)])  # (current value of x, number of operations)
                visited = set()  # To avoid revisiting the same state

                while queue:
                    curr, steps = queue.popleft()

                    # If we've reached the target value y
                    if curr == y:
                        return steps

                    # Mark the current state as visited
                    if curr in visited:
                        continue
                    visited.add(curr)

                    # Generate possible next moves
                    if curr % 11 == 0:
                        queue.append((curr // 11, steps + 1))
                    if curr % 5 == 0:
                        queue.append((curr // 5, steps + 1))
                    queue.append((curr - 1, steps + 1))
                    queue.append((curr + 1, steps + 1))

                # This line should never be reached since there's always a valid solution
                return -1
