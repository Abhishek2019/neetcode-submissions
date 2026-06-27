class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        # Build adjacency as min-heaps so we can always take smallest destination next
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(u: str) -> None:

            while graph[u]:
                v = heapq.heappop(graph[u])
                dfs(v)

            route.append(u)

        dfs("JFK")
        return route[::-1]
