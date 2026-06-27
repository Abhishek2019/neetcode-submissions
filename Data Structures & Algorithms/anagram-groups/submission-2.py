from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out_map = {}
        for str in strs:

            temp_set = frozenset(Counter(str).items())

            if temp_set not in out_map:
                out_map[temp_set] = [str]

            else:
                out_map[temp_set].append(str)


        return [val for val in out_map.values()]

            