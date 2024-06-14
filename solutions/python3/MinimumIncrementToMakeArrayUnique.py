class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            if nums[i] <= prev:
                res += prev + 1 - nums[i]
                nums[i] = prev + 1
        return res
