class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        res = max_val = cur_len = 0

        for num in nums:
            if max_val < num:
                max_val = num
                cur_len = 0
                res = 0
            if num == max_val:
                cur_len += 1
            else:
                cur_len = 0
            
            res = max(res, cur_len)

        return res

        
        # initial solution:
        
        # max_val = max(nums)

        # # find longest contiguous subarray with max_val only
        # left = res = 0
        # for right in range(len(nums)):
        #     if nums[right] == max_val:
        #         while nums[left] != max_val:
        #             left += 1
        #         res = max(res, right - left + 1)
        #     else:
        #         left = right

        # return res
