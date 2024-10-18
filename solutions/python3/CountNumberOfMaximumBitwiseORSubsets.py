class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        max_or = 0
        for num in nums:
            max_or |= num

        res = 0
        def dfs(i, cur_or):
            nonlocal max_or, res
            if i == len(nums):
                res += 1 if cur_or == max_or else 0
                return
            dfs(i + 1, cur_or)
            dfs(i + 1, cur_or | nums[i])

        dfs(0, 0)
        return res
