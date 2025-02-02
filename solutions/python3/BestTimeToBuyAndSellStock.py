class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0
        
        min_so_far = float('inf')
        res = -1
        for price in prices:
            min_so_far = min(min_so_far, price)
            res = max(res, price - min_so_far)

        return res
