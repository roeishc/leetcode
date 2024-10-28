class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        checked = set()
        res = -1

        max_val = max(nums)
        for num in nums:
            if num in checked:
                continue
            streak = 0
            temp = num
            while temp in nums_set and temp <= max_val:
                streak += 1
                checked.add(temp)
                temp *= temp
            if streak >= 2:
                res = max(res, streak)

        return res
