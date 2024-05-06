class Solution:
    def value(self, sym: str) -> int:
        if sym == 'I':
            return 1
        if sym == 'V':
            return 5
        if sym == 'X':
            return 10
        if sym == 'L':
            return 50
        if sym == 'C':
            return 100
        if sym == 'D':
            return 500
        if sym == 'M':
            return 1000
        return -1

    def romanToInt(self, s: str) -> int:
        res = 0
        str_len = len(s)
        i = 1
        for _ in range(0, str_len):
            res += self.value(s[-i])
            if (s[-i] == 'V' or s[-i] == 'X') and i < str_len and s[-i-1] == 'I':
                res -= 1
                i += 1
            if (s[-i] == 'L' or s[-i] == 'C') and i < str_len and s[-i-1] == 'X':
                res -= 10
                i += 1
            if (s[-i] == 'D' or s[-i] == 'M') and i < str_len and s[-i-1] == 'C':
                res -= 100
                i += 1
            if i >= str_len:
                break
            i += 1
        return res