class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        freqs = defaultdict(int)
        for s in arr:
            freqs[s] += 1

        count = 1
        for s, freq in freqs.items():
            if freq == 1:
                if count == k:
                    return s
                count += 1
            
        return ""
