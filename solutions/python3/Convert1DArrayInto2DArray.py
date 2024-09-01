class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if n * m != len(original):
            return []

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            res[i][:] = original[i * n : (i + 1) * n]
        
        return res
