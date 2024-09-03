class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        total = 0
        for c in s:
            val = str(ord(c) - ord('a') + 1)
            for digit in val:   # either 1 or 2 digits
                total += int(digit)

        if k == 1:
            return total
        
        for _ in range(k - 1):
            res = 0
            while total > 0:
                res += total % 10
                total //= 10
            total = res

        return res
        
        
        # initial solution: O(n) space

        # nums = ""
        # for c in s:
        #      nums += str(ord(c) - ord('a') + 1)
        
        # for _ in range(k):
        #     res = 0
        #     for c in nums:
        #         res += int(c)
        #     nums = str(res)
        
        # return res
