import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        routes = []
        
        def dfs(src):
            nonlocal routes

            while graph[src]:
                dest = heapq.heappop(graph[src])
                dfs(dest)

            routes.append(src)

        dfs("JFK")
        return routes[::-1]

            




        


        