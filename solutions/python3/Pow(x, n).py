class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0 and n > 0:
            return 0
        
        if n == 0 and x > 0:
            return 1

        if x == 1:
            return 1

        if x == -1:
            return -1 if n % 2 == 1 else 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        res: float = 1

        while n > 0:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                res *= x
                n -= 1
            if res == 0:
                return 0

        return res
        