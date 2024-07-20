class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        rows = len(rowSum)
        cols = len(colSum)

        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                res[i][j] = min(rowSum[i], colSum[j])
            
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        
        return res
        