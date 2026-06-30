from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.map[key][timestamp] = value 
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""
        
        if timestamp in self.map[key]:

            return self.map[key][timestamp]
        
        search_list = sorted(self.map[key].keys())

        if timestamp < search_list[0]:
            return ""

        if timestamp > search_list[-1]:
            return self.map[key][search_list[-1]]


        l = 0
        r = len(search_list)-1
        ans = -1
        while l<=r:

            mid = (l+r)//2

            if search_list[mid] > timestamp:
                r = mid-1
            else:
                ans = mid
                l = mid+1

        if ans == -1:
            return ""



        return self.map[key][search_list[ans]]



        
