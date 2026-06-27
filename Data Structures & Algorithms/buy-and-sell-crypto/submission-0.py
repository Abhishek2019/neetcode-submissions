class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        n = len(prices)

        min_price = prices[0]

        for i in range(1,n):

            print(prices[i], min_price, max_profit)

            if prices[i] > min_price:

                curr_profit = prices[i] - min_price

                if curr_profit > max_profit:
                    max_profit = curr_profit

            else:
                min_price = prices[i]

        return max_profit



