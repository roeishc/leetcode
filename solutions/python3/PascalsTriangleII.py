class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        prev = [1]

        for _ in range(rowIndex):
            res = [1] * (len(prev) + 1)
            res[0], res[-1] = prev[0], prev[-1]
            for i in range(1, len(res) - 1):
                res[i] = prev[i - 1] + prev[i]
            prev = res

        return res
