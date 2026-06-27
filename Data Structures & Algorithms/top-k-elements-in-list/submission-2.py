from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}

        for ele in nums:
            count_map[ele] = 1+count_map.get(ele,0)

        freq = [[] for _ in range(len(nums)+1)]


        for key,val in count_map.items():
            freq[val].append(key)

        print(freq)

        res = []
        for out_ele in freq[::-1]:

            if len(res)<k:
                if out_ele:
                    res+=out_ele
            else:
                return res
            



