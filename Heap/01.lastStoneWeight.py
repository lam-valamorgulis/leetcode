# https://leetcode.com/problems/kth-largest-element-in-a-stream/


import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k

        # turn arr to minHeap using heapify()
        heapq.heapify(self.minHeap)

        # maintain the minHeap only for K element
        # it will return the kth largest element
        while len(self.minHeap) > k :
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
















