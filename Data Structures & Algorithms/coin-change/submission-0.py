class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [amount+1]*(amount+1)

        dp[0] = 0

        for curr_amt in range(1,amount+1):

            for co in coins:

                if curr_amt-co >=0:

                    dp[curr_amt] = min(dp[curr_amt], 1+dp[curr_amt-co])


        return dp[amount] if dp[amount]!= amount+1 else -1