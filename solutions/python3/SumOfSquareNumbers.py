class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        big = int(sqrt(c)) + 1
        small = 0

        while small <= big:
            small_s = small ** 2
            big_s = big ** 2
            if small_s + big_s > c:
                big -= 1
            elif small_s + big_s < c:
                small += 1
            else:
                return True
        
        return False
