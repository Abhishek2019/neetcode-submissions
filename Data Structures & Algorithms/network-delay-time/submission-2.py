from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # edges_len = len(times)

        graph = defaultdict(list)

        for src, dst, cost in times:
            graph[src].append((cost, dst))

        
        frontier = [[0,k]]

        min_cost_to_reach = [float('inf')]*(n+1)

        min_cost_to_reach[k] = 0

        visited = set()

        while frontier:

            cost, src = heapq.heappop(frontier)

            if src in visited:
                continue
            
            visited.add(src)

            if min_cost_to_reach[src] != cost or min_cost_to_reach[src]==float('inf') :
                continue

            if len(visited) == n:
                return cost


            for dist, dest in graph[src]:

                ndist = dist+cost

                if ndist < min_cost_to_reach[dest]:
                    min_cost_to_reach[dest] = ndist

                if dest not in visited:
                    heapq.heappush(frontier,[ndist,dest])


        return -1


            



