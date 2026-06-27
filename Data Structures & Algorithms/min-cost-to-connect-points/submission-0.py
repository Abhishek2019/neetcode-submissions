import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        graph = defaultdict(list)

        for i in range(n):
            for j in range(i+1,n):

                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])

                graph[i].append((dist,j))
                graph[j].append((dist,i))

        res = 0
        visit = set()
        minH = [[0,0]]

        while len(visit) < n:
            cost,i=heapq.heappop(minH)
            if i in visit:
                continue
            res+=cost
            visit.add(i)

            for ncost, ni in graph[i]:
                if ni not in visit:
                    heapq.heappush(minH,[ncost,ni])

        return res



