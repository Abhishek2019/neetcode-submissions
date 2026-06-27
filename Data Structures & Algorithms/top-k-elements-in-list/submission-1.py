from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        d = defaultdict(int)

        
        for i in nums:

            d[i]+=1

        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        for nu, f in d.items():

            bucket[f].append(nu)

        print(bucket)
        out = []
        for i in range(n, -1,-1):
            print("idx",i)
            if bucket[i] and k>0:

                out+=(bucket[i])
                k-=len(bucket[i])

        return out




        