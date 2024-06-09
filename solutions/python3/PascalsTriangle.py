class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res: List[List[int]] = []
        res.append([1])
        row = [1]
        next_row = deepcopy(row)

        for i in range(1, numRows):
            next_row_len = len(row) + 1
            next_row = [0] * next_row_len
            
            next_row[0] = row[0]   # first element
            next_row[next_row_len - 1] = row[next_row_len - 2]   # last element
            for j in range(1, next_row_len - 1):  # elements between first and last
                next_row[j] = row[j - 1] + row[j]
            
            res.append(next_row)
            row = next_row
        
        return res
