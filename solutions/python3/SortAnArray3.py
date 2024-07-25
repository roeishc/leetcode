class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        return self._counting_sort(nums)


    def _counting_sort(self, nums: List[int]) -> List[int]:

        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        min_val = min(nums)
        max_val = max(nums)
        
        res = [0] * len(nums)
        i = 0

        for val in range(min_val, max_val + 1):
            while freqs[val] > 0:
                res[i] = val
                freqs[val] -= 1
                i += 1
        
        return res
        