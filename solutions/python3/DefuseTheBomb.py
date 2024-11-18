class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        if k == 0:
            return [0] * len(code)

        N = len(code)
        res = [0] * N
        
        if k > 0:
            window_sum = 0
            i = 1
            while i < k + 1:
                window_sum += code[i % N]
                i += 1
            for i in range(N):
                res[i] = window_sum
                window_sum -= code[(i + 1) % N]
                window_sum += code[(i + 1 + k) % N]
        else:
            return self.decrypt(code[::-1], -k)[::-1]
        
        return res
