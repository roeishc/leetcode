class Solution:
    def minimumSteps(self, s: str) -> int:
        
        left, right = 0, len(s) - 1

        res = 0
        while left < right:
            if s[left] == '1':
                if s[right] == '0':
                    res += right - left
                    left += 1
                right -= 1
            else:
                if s[right] == '1':
                    right -=1
                left += 1
        
        return res

