class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        max_to_my_right = [0] * n
        max_to_my_right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            max_to_my_right[i] = max(nums[i], max_to_my_right[i + 1])

        res = left = 0
        for right in range(n):
            while left <= right and nums[left] > max_to_my_right[right]:
                left += 1
            res = max(res, right - left)
        
        return res
