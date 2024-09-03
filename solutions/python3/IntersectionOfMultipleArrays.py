class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        freqs = defaultdict(int)
        for arr in nums:
            for num in arr:
                freqs[num] += 1
        
        n = len(nums)
        res = []
        for num, freq in freqs.items():
            if freq == n:
                res.append(num)
        res.sort()

        return res
