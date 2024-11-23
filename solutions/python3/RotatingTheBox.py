class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        ROWS, COLS = len(box), len(box[0])

        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == '#':    # stone
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == '*':  # obstacle
                    i = c - 1

        res = []

        for c in range(COLS):
            res_col = []
            for r in range(ROWS):
                res_col.append(box[r][c])
            res_col.reverse()
            res.append(res_col)

        return res
