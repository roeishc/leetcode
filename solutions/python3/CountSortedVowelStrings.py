class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * 5 for i in range(n)]
        for row in range(1, n):
            temp = 0
            for col in range(5):
                temp += dp[row - 1][4 - col]
                dp[row][4 - col] = temp
        res = 0
        for i in range(5):
            res += dp[n - 1][i]
        return res
        