import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = [sqrt((i[0]-0)**2+(i[1]-0)**2) for i in points]
 

        heap = list(zip(dist, points))

        heapq.heapify(heap)
        out = []
        for _ in range(k):
            out.append(heapq.heappop(heap)[1])
        return out
        