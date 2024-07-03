class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0

        maxs = sorted(heapq.nlargest(4, nums))
        mins = sorted(heapq.nsmallest(4, nums))

        res = float('inf')
        for i in range(4):
            res = min(res, maxs[i] - mins[i])
        
        return res        
        
        
        # first iteration of my solution: passes only some tests
        # greedily removes largest absolute value between min,max in nums
        # doesn't check for differences between elements
        
        # if len(nums) <= 4:
        #     return 0

        # cpy = deepcopy(nums)
        # for _ in range(3):
        #     temp_max = max(cpy)
        #     temp_min = min(cpy)
        #     if abs(temp_max) > abs(temp_min):
        #         cpy.remove(temp_max)
        #     else:
        #         cpy.remove(temp_min)
        
        # return max(cpy) - min(cpy)
