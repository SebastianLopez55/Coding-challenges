
def maxProfit(prices):
    maxP = 0
    L, R = 0, 1
    while R < len(prices):
        currP = prices[R] - prices[L]
        maxP = max(maxP, currP)
        while R < len(prices) and prices[R] < prices[L]:
            L += 1
            R = L + 1
        R += 1
    return maxP


print(maxProfit([7, 1, 5, 3, 6, 4]))


print(maxProfit([7 ,6 ,4 ,3 ,1]))
