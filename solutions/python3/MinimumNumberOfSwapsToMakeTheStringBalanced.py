class Solution:
    def minSwaps(self, s: str) -> int:
        
        closing = opening = 0
        max_extra_closing = 0

        for c in s:
            if c == '[':
                opening += 1
            else:
                closing += 1
            max_extra_closing = max(max_extra_closing, closing - opening)

        return ceil(max_extra_closing / 2)
