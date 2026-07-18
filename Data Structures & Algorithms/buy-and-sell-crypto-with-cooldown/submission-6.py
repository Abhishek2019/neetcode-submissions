class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,status):

            s1,s2,s3,s4,s5 = 0,0,0,0,0

            

            if (i,status) in dp:
                return dp[(i,status)]
            if i >=len(prices):
                return 0

            if status == "buy":
                s1 = dfs(i+1,"buy")
                s2 = dfs(i+1,"sell")-prices[i]

            elif status == "sell":
                s3 = dfs(i+1, "sell")
                s4 = dfs(i+1,"skip")+prices[i]

            else:
                s5 = dfs(i+1, "buy")

            dp[(i,status)] = max(s1,s2,s3,s4,s5) 
            return dp[(i,status)]



        out = dfs(0,"buy")
        return out