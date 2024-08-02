class Solution:
    def minSwaps(self, nums: List[int], total_ones = None) -> int:
        
        n = len(nums)
        max_window_ones = window_ones = 0
        left = 0
        total_ones = nums.count(1)

        for right in range(2 * n):
            if right - left + 1 > total_ones:   # if window's length is greater than total ones
                window_ones -= nums[left % n]   # decrement if one is leftmost element
                left += 1
            if nums[right % n] == 1:
                window_ones += 1
            max_window_ones = max(max_window_ones, window_ones)
            
        return total_ones - max_window_ones

        
        # initial solution

        # first_one = -1
        # last_one = -1

        # if total_ones is None:  # pass an additional parameter to avoid counting ones twice (or more) in recursive call
        #     total_ones = 0
        #     for i, num in enumerate(nums):
        #         if num == 1:
        #             last_one = i
        #             total_ones += 1
        #             if first_one == -1:
        #                 first_one = i
                
        # if (
        #     total_ones == 0 or
        #     last_one == first_one or
        #     len(nums) < 3
        #     ):
        #     return 0

        # if nums[0] == 1 and nums[-1] == 1:
        #     return self.minSwaps(nums[1:len(nums)-1], total_ones - 2)

        # return last_one - first_one + 1 - total_ones
