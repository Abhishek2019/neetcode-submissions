class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = {}

        def dfs(lc,rc, curr_seq):

            if (lc,rc, curr_seq) in dp:
                return dp[(lc,rc, curr_seq)] 
            if lc>=len(text1):
                return curr_seq

            if rc >= len(text2):
                return curr_seq

            if text1[lc] == text2[rc]:
                
                return dfs(lc+1, rc+1,curr_seq+1)

            s1 = dfs(lc,rc+1, curr_seq)
            s2 = dfs(lc+1,rc, curr_seq)

            max_len = max(s1,s2)
            dp[(lc,rc, curr_seq)] = max_len
            return max_len


        out = dfs(0,0,0)

        return out