# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM


MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Create adjacency list for the graph
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Dijkstra's algorithm setup
        min_time = [float('inf')] * n  # To store the shortest time to each node
        ways = [0] * n                 # To store the number of ways to reach each node in the shortest time
        min_time[0] = 0                # Time to reach node 0 is 0
        ways[0] = 1                    # There's 1 way to reach node 0 (by starting there)
        
        # Priority queue to explore nodes (time, node)
        pq = [(0, 0)]  # (current shortest time, node)
        
        while pq:
            time, node = heapq.heappop(pq)
            
            # If the time to reach this node is longer than the already found shortest time, skip it
            if time > min_time[node]:
                continue
            
            # Explore the neighbors
            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time
                
                # If we find a shorter path to the neighbor
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]  # Inherit the number of ways from the current node
                    heapq.heappush(pq, (new_time, neighbor))
                
                # If we find another shortest path to the neighbor
                elif new_time == min_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        # The number of ways to reach node n-1 in the shortest time
        return ways[n-1]

