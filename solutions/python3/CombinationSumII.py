class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # take only the candidates less than target
        relevant = deepcopy(candidates)
        relevant.sort()
        first_gt = self.find_first_gt(relevant, target)
        if first_gt > 0:
            relevant = relevant[0:first_gt]
        else:
            return []

        res = []

        def backtrack(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or idx == len(relevant):
                return
            
            cur.append(relevant[idx])
            backtrack(idx + 1, cur, total + relevant[idx])
            cur.pop()

            while idx + 1 < len(relevant) and relevant[idx] == relevant[idx + 1]:
                idx += 1
            backtrack(idx + 1, cur, total)

        backtrack(0, [], 0)
        return res
                

    def find_first_gt(self, nums: List[int], value) -> int:
        for i, num in enumerate(nums):
            if num > value:
                return i
        return len(nums)
