class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        min_price1 = float('inf')
        min_price2 = float('inf')

        for price in prices:
            if price < min_price1:
                min_price2 = min_price1
                min_price1 = price
            elif price < min_price2:
                min_price2 = price

        leftover = money - (min_price1 + min_price2)
        
        return max(leftover, 0)
    