# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Build the graph as an adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Helper function: Dijkstra's algorithm to find shortest distances from a source node
        def dijkstra(source):
            dist = [float('inf')] * n
            dist[source] = 0
            min_heap = [(0, source)]  # (distance, node)
            
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                
                # If we find a longer distance than known, skip
                if current_dist > dist[u]:
                    continue
                
                # Visit all neighbors of u
                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(min_heap, (dist[v], v))
            
            return dist

        # Step 2: For each city, use Dijkstra to calculate the number of reachable cities
        min_reachable_cities = float('inf')
        result_city = -1
        
        for city in range(n):
            dist_from_city = dijkstra(city)
            reachable_cities_count = sum(1 for d in dist_from_city if d <= distanceThreshold and d != float('inf'))
            
            # Step 3: Update the result based on the criteria
            if reachable_cities_count < min_reachable_cities:
                min_reachable_cities = reachable_cities_count
                result_city = city
            elif reachable_cities_count == min_reachable_cities:
                result_city = max(result_city, city)  # Break tie by choosing the city with the greatest index

        return result_city
