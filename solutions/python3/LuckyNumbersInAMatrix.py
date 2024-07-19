import numpy as np

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        row_mins = []
        col_maxs = []

        rows = len(matrix)
        cols = len(matrix[0])

        mat = np.array(matrix)

        for i in range(rows):
            row_mins.append(min(mat[i, :]))

        for i in range(cols):
            col_maxs.append(max(mat[:, i]))

        res = []
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == row_mins[row] and mat[row][col] == col_maxs[col]:
                    res.append(mat[row][col])

        return res
