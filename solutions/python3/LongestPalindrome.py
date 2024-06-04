class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq: dict = defaultdict(int)
        for c in s:
            freq[c] += 1

        total: int = 0
        is_extra: bool = False
        for k, v in freq.items():
            if v % 2 == 0:
                total += v
            else:
                total += v - 1
                is_extra = True
        
        if is_extra:
            return total + 1
        return total