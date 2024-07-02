class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        freqs1 = defaultdict(int)
        freqs2 = defaultdict(int)

        for num in nums1:
            freqs1[num] += 1

        for num in nums2:
            freqs2[num] += 1
        
        res = []
        for num, freq in freqs1.items():
            while freq > 0 and freqs2[num] > 0:
                res.append(num)
                freq -= 1
                freqs2[num] -= 1
        
        return res
