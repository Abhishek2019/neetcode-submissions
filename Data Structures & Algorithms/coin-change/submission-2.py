class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(curr_amt):

            if curr_amt<0:
                return float('inf')

            if curr_amt in dp:
                return dp[curr_amt]
            if curr_amt == 0:
                return 0

            min_coins = float('inf')
            for coin in coins:
                st1 = 1+dfs(curr_amt-coin)
                min_coins = min(min_coins,st1)

            dp[curr_amt] = min_coins
            return min_coins


        
        out = dfs(amount)

        if out == float('inf'):
            return -1
        return out