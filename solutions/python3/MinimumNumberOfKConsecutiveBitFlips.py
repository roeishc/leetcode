class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        flipped = [False] * n
        validFlipsFromPastWindow = 0
        res = 0

        for i in range(n):
            if i >= k and flipped[i - k]:       # after advancing the sliding window (k), if the last bit
                                                # that went out was flipped, decrement how many flipped bits
                validFlipsFromPastWindow -= 1   # there are currently in the window
            if nums[i] == validFlipsFromPastWindow % 2: # either 0 and 0, or 1 and 1. both require flips
                if n < i + k:   # if current bit needs to flip, but window goes past array's length
                    return -1
                validFlipsFromPastWindow += 1
                res += 1
                flipped[i] = True
        
        return res
