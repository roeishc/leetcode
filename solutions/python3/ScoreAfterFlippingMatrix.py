class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        col_len: int = len(grid)
        res: int = 0

        for row in range(col_len):  # flip msb in each row to 1
            if grid[row][0] == 0:
                self.flip_row(grid, row)

        for i in range(1, len(grid[0])):  # in each col, at least half should be 1's
            if self.count_ones_in_col(grid, i) < col_len / 2:
                self.flip_col(grid, i)

        for i in range(col_len):  # count the result
            res += self.row_to_int(grid, i)

        return res

    def count_ones_in_col(self, grid: List[List[int]], col: int) -> int:
        res: int = 0
        for i in range(len(grid)):
            res += grid[i][col]
        return res

    def row_to_int(self, grid: List[List[int]], row: int) -> int:
        row_len: int = len(grid[0])
        res: int = 0
        for i in range(row_len):
            res += grid[row][i] << (row_len - i - 1)
            # res += grid[row][i] * (2 ** (row_len - i - 1))    # slower
        return res

    def flip_col(self, grid: List[List[int]], col: int):
        for i in range(len(grid)):
            grid[i][col] ^= 1

    def flip_row(self, grid: List[List[int]], row: int):
        for i in range(len(grid[0])):
            grid[row][i] ^= 1
