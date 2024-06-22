class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        start = 0
        odds = 0
        gap = 0
        res = 0

        for end in range(len(nums)):
            if nums[end] %2 == 1:
                odds += 1
            if odds == k:
                gap = 0
                while odds == k:
                    odds -= nums[start] % 2 # no change if nums[start] is even
                    gap += 1
                    start += 1
            res += gap
        
        return res


        # First iteration of my solution - inefficient, O(n^2)

        # n = len(nums)
        # res = 0

        # for i, start in enumerate(nums):
        #     end = i
        #     odds = 0
        #     while end < n and odds < k:
        #         if nums[end] % 2 == 1:
        #             odds += 1
        #         end += 1
        #     if odds == k:
        #         res += 1
        #     while end < n and nums[end] % 2 == 0:
        #         res += 1
        #         end += 1

        # return res
            