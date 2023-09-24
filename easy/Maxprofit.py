def maxProfit(prices: list) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    # check if the diff between two positions in the biggest we have seen
    # number_checked = 0
    # max_profit = 0
    # for i in range(len(prices)):
    #     if prices[number_checked] <= prices[i]:
    #         max_profit = max(max_profit, prices[i] - prices[number_checked])
    #     else:
    #         number_checked = i
    # return max_profit

    maximum_profit = 0
    lowest_price = prices[0]

    for day in range(len(prices)):
        lowest_price = min(prices[day], lowest_price)
        price_difference = prices[day] - lowest_price
        maximum_profit = max(price_difference,maximum_profit)
    return maximum_profit

print(maxProfit(prices = [1,2,3,4,5,6,7,8,9]))