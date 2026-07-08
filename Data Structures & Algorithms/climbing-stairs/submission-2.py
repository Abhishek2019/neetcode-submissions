class Solution:
    def climbStairs(self, n: int) -> int:
        # slolved by dfs
        map = {}
        def dfs(i):

            if i>n:
                return 0

            if i in map:
                return map[i]

            s1 = dfs(i+1)
            s2 = dfs(i+2)

            if i==n:
                map[i] = 1+s1+s2 
                return 1+s1+s2
            
            map[i] = s1+s2
            return s1+s2

            




        out = dfs(0)
        return out

        # solved by dp