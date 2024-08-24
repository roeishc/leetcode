class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        len_n = len(n)
        
        i = len(n) // 2
        if len_n % 2 == 0:
            i -= 1
        
        first_half = int(n[: i + 1])

        possibilities = []

        for j in range(-1, 2, 1):
            possibilities.append(
                self.half_to_palindrome(first_half + j, len(n) % 2 == 0)
            )
        possibilities.append(10 ** (len_n - 1) - 1) # 999...999 case
        possibilities.append(10 ** len_n + 1) # 100...001 case

        min_diff = float('inf')
        res, num = 0, int(n)

        for candidate in possibilities:
            if candidate == num:
                continue
            if abs(candidate - num) < min_diff:
                min_diff = abs(candidate - num)
                res = candidate
            elif abs(candidate - num) == min_diff:
                res = min(res, candidate)

        return str(res)


    def half_to_palindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left //= 10
        while left > 0:
            res = res * 10 + left % 10  # "append" the smallest digit of `left` to `res`
            left //= 10
        return res
        