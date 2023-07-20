## Array
## DP
## Greedy

### Date: 07/19/2023

#### Citadel

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        #starting from day 2
        for i in range(1,len(prices)):
            # check if today's price is higher than yesterday's price
            # if true, buy yesterday and sell today(add today's price - yesterday's price to profit)
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit

## TC: O(n)
##SC: O(1)