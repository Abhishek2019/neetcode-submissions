class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        r = 0

        check = set()
        out = 0
        final_out = 0
        while r<len(s):

            if not check or s[r] not in check:
                check.add(s[r])
                out+=1
                r+=1

            else:
                final_out = max(final_out, out)
                while check and s[r] in check:

                    check.remove(s[l])
                    l+=1
                    out-=1

        final_out = max(final_out, out)


        return final_out
            