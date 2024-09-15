class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        res = mask = 0
        mask_to_idx = {0: -1}

        for i, c in enumerate(s):
            if c in vowels:
                mask ^= 1 + ord(c) - ord('a')
            if mask in mask_to_idx:
                res = max(res, i - mask_to_idx[mask])
            else:
                mask_to_idx[mask] = i
        
        return res
