class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def dfs(i,status, curr_profit):

            if (i,status, curr_profit) in dp:
                return dp[(i,status, curr_profit)]
            
            if i>=len(prices):
                return curr_profit

            

            s1,s2,s3,s4,s5 = float('-inf'),float('-inf'),float('-inf'),float('-inf'),float('-inf')
            if status == "buy":
                s1 = dfs(i+1,"buy",curr_profit)
                s2 = dfs(i+1,"sell",curr_profit-prices[i])

            elif status == "sell":

                s3 = dfs(i+1,"sell",curr_profit)
                s4 = dfs(i+1,"skip",curr_profit+prices[i])              
            
            else:
                s5 = dfs(i+1,"buy",curr_profit)

            dp[(i,status, curr_profit)] = max(curr_profit, s1,s2,s3,s4,s5) 
            return  dp[(i,status, curr_profit)]



        out = dfs(0,"buy",0)
        return out