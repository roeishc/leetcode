class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        count = defaultdict(int)

        for row in matrix:
            row_key = tuple(row)
            if row_key[0]:  # if starting with 1, flip it
                row_key = tuple([0 if n == 1 else 1 for n in row])
            count[row_key] += 1
        
        return max(count.values())
