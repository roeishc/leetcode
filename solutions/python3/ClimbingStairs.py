class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2

        one = 1
        two = 2

        for i in range(2, n):
            # dp[i] = dp[i - 1] + dp[i - 2]
            temp = one + two
            one = two
            two = temp

        # return dp[-1]
        return temp
