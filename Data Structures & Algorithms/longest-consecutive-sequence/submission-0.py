class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)

        if not nums:
            return 0

        ns = set(nums)

        longest = 0

        for i in ns:

            if i-1 not in ns:

                curr = i
                curr_long = 1
                
                while curr+1 in ns:
                    curr_long+=1
                    curr+=1

                longest = max(longest, curr_long)

        return longest
