class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        # same result can be achieved with: freqs = Counter(nums)
        
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        freqs = {k: v for k, v in sorted(freqs.items(), key=lambda item: (item[1], -item[0]))}

        res = []
        for num, count in freqs.items():
            while count > 0:
                res.append(num)
                count -= 1
        
        return res
