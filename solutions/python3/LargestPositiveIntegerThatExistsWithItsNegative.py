class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res: int = -1
        for num in nums:
            if num > res and -num in nums:
                res = num
        return res