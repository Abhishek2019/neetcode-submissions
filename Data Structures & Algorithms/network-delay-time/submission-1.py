import heapq
from collections import defaultdict
import numpy as np

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for u,v,d in times:

            graph[u].append((v,d))
        
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        visited = [0]*(n+1)
        visited[0] = 1
    
        q = [(0,k)]

        while q:

            d, node = heapq.heappop(q)

            if visited[node] == 1:
                continue
            
            visited[node] = 1

            for child, child_dist in graph[node]:

                nd = d+child_dist

                if nd < dist[child]:
                    dist[child] = nd
                    heapq.heappush(q, (nd, child))

        
        if 0 in visited:
            return -1
        else:
            return max(dist[1:])
                


