class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        out_set = set(nums)

        longest = 0

        for i in out_set:

            if (i-1) not in out_set:
                length=1

                while (i+length) in out_set:
                    length+=1

                
                longest = max(longest,length)
        return longest



