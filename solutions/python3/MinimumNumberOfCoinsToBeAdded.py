class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
        coins.sort()
        res = 0
        N = len(coins)
        i = 0
        next_val = 1

        while next_val <= target:
            if i < N and coins[i] <= next_val:
                next_val += coins[i]
                i += 1
            else:
                next_val += next_val
                res += 1
        
        return res
