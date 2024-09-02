class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        if k >= total:
            k %= total
        
        prefix_sum = i = 0
        
        while prefix_sum < k:
            prefix_sum += chalk[i]
            if prefix_sum > k:
                return i
            i += 1
        
        return i

        
        # initial solution: 

        # if len(chalk) == 1:
        #     return 0
        
        # total = sum(chalk)
        # if k >= total:
        #     k = k % total
        
        # i = 0
        # # while k > 0:
        # for i, chalk_required in enumerate(chalk):
        #     print(f"i={i}, chalk_required={chalk_required}, remaining={k}")
        #     if k >= chalk_required:
        #         k -= chalk_required
        #     else:
        #         return i
        
        # return i % (len(chalk) - 1)
