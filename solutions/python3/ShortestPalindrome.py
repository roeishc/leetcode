class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        prefix = suffix = 0
        base = 29   # prime larger than 26 (for the entire English alphabet) to help with collisions
        last_index = 0
        mod = 10**9 + 7

        power = 1
        for i, c in enumerate(s):
            current = ord(c) - ord('a') + 1 # map to [1, 26]

            prefix = (prefix * base) % mod  # may overflow if very large, can mod by large prime (smaller than 32bit) like 10**9 + 7
            prefix = (prefix + current) % mod

            suffix = (suffix + current * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                last_index = i
            
        non_repeated = s[last_index + 1:]
        return non_repeated[::-1] + s
