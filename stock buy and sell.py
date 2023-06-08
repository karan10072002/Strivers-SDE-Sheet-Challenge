def maximumProfit(prices):
    profit = 0
    minimum, maximum = prices[0], prices[0]
    for i in range(len(prices)):
        if prices[i] < minimum:
            minimum = prices[i]
            maximum = 0
        elif prices[i]> maximum:
            maximum = prices[i]
            if (maximum - minimum)>profit:
                profit = maximum - minimum
    return profit
