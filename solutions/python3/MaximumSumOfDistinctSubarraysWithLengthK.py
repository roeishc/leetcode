class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        last_seen = {}
        res = cur_sum = 0

        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            i = last_seen.get(nums[r], -1)
            while l <= i or r - l + 1 > k:
                cur_sum -= nums[l]
                l += 1
            if r - l + 1 == k:
                res = max(res, cur_sum)
            last_seen[nums[r]] = r
        
        return res
            