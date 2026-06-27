import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        graph = defaultdict(list)

        for i in range(n):

            sx,sy = points[i]

            for j in range(i+1,n):

                dx,dy = points[j]

                cost = abs(sx-dx)+abs(sy-dy)

                graph[i].append((cost,j))
                graph[j].append((cost,i))

        
        
        currCost = 0
        minH = [(0,0)]
        visited=set()

        while minH:

            cost, node = heapq.heappop(minH)


            if node in visited:
                continue

            currCost+=cost
            visited.add(node)

            if len(visited) == n:
                return currCost

            for c, ch in graph[node]:
                
                if ch not in visited:
                    heapq.heappush(minH, (c,ch))

        return -1









        
