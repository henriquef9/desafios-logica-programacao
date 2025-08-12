

def maxProfit(prices):

    min_price = 0
    max_profit = 0
    for i in range(1,len(prices)):
        
        if prices[min_price] > prices[i]:
            min_price = i
        profit = prices[i] - prices[min_price]
        max_profit = max(max_profit, profit)
    
    return max_profit
