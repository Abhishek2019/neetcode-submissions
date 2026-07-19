class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}

        def dfs(i, curr_amt):

            if (i,curr_amt) in dp:
                return dp[(i,curr_amt)]

            if curr_amt == 0:
                return 1

            if curr_amt < 0 or i >= len(coins):
                return 0
                
            
            s1 = dfs(i+1, curr_amt)
            s2 = dfs(i,curr_amt-coins[i])
            dp[(i,curr_amt)] = s1+s2
            return s1+s2

            

        return dfs(0,amount)