class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        a = b = 0
        for c in s:
            if c == "a":
                a += 1
        
        res = float('inf')
        for c in s:
            if c == "a":
                a -= 1
            res = min(res, a + b)
            if c == "b":
                b += 1
        
        return res
