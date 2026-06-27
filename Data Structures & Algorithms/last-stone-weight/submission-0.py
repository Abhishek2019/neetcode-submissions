import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >1:

            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x == y:
                pass
            elif x < y:
                heapq.heappush(maxHeap,-(y-x))
            else:
                heapq.heappush(maxHeap,-(x-y))
        if len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)
        return 0


