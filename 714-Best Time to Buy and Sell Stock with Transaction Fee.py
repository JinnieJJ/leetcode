class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, bought = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, bought + prices[i] - fee)
            bought = max(bought, cash - prices[i])
        return cash
