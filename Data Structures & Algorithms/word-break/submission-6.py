class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        search = set(wordDict)
        dp = {}

        def dfs(l,r):
            
            if r> len(s):
                return False

            if r ==len(s):
                if s[l:r] not in search:

                    return False

                else:

                    return True

            if (l,r) in dp:
                return dp[(l,r)]
            if s[l:r] not in search:
                st1 = dfs(l,r+1)

            else:
                st1 = dfs(r,r+1) or dfs(l,r+1)

            dp[(l,r)] = st1
            return st1


        out = dfs(0,1)
        return out