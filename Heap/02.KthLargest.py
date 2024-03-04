# https://leetcode.com/problems/last-stone-weight/

# Time Complexity:

# The initialization step takes O(n) time.
# In each iteration of the while loop, we perform two heapq.heappop() operations and one heapq.heappush() operation. These operations each have a time complexity of O(log n), where n is the number of elements in the heap.
# Therefore, the overall time complexity of the main loop is O(k log n), where k is the number of elements in the stones list.
# Since the initialization step and the main loop are both O(n) and O(k log n) respectively, the dominant factor in the time complexity is O(k log n).
# So, the overall time complexity of the provided solution is O(n + k log n).


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python dont have max_heap
        # convert by multiply -1 
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = abs(heapq.heappop(max_heap))
            second = abs(heapq.heappop(max_heap))

            if second < first :
                # 8 - 7 = 1 convert to max_heap by * - 1
                heapq.heappush(max_heap, -1 * (first - second))

        return 0 if not max_heap else abs(max_heap[0])















