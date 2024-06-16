class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        N = len(nums)
        next_val = 1
        res = 0
        i = 0

        while next_val <= n:
            if i < N and nums[i] <= next_val:
                next_val += nums[i]
                i += 1
            else:
                next_val += next_val
                res += 1
        
        return res