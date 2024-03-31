# https://leetcode.com/problems/cheapest-flights-within-k-stops/



import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create adjancey node list
        # Create an adjacency list representation of the graph
        graph = {}
        for flight in flights:
            start, end, price = flight
            if start not in graph:
                graph[start] = []
            graph[start].append((end, price))

        # Dijkstra's algorithm
        heap = [(0, src, 0)]  # (price, city, stops)
        visited = set()
        while heap:
            price, city, stops = heapq.heappop(heap)
            if city == dst:
                return price
            if stops > k or (city, stops) in visited:
                continue
            visited.add((city,stops))
            if city in graph:
                for neighbor, neighbor_price in graph[city]:
                    heapq.heappush(heap, (price + neighbor_price, neighbor, stops + 1))

        return -1





