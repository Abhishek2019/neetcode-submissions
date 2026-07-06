import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        out = [ (math.sqrt(point[0]**2 + point[1]**2),point) for point in points ]
        print(out)
        heapq.heapify(out)

        ans = []
        while k>0:
            ans.append(heapq.heappop(out)[1])
            k-=1

        return ans