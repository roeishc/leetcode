class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0
        
        res = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [row[j:j+3] for row in grid[i:i+3]]
                if self._is_magic_square(subgrid):
                    res += 1
        
        return res


    def _is_magic_square(self, grid: List[List[int]]) -> bool:  # expecting a 3x3 input grid
        # check distinct numbers
        nums = [0] * 10
        for row in range(3):
            for col in range(3):
                if grid[row][col] > 0 and grid[row][col] < 10:
                    if nums[grid[row][col]] != 0:
                        return False
                    nums[grid[row][col]] = grid[row][col]
                else:
                    return False

        # check sum of each each
        total = sum(grid[0])
        if (
            sum(grid[1]) != total or    # row 1
            sum(grid[2]) != total or    # row 2
            grid[0][0] + grid[1][0] + grid[2][0] != total or    # col 0
            grid[0][1] + grid[1][1] + grid[2][1] != total or    # col 1
            grid[0][2] + grid[1][2] + grid[2][2] != total or    # col 2
            grid[0][0] + grid[1][1] + grid[2][2] != total or    # diagonal
            grid[2][0] + grid[1][1] + grid[0][2] != total       # diagonal
            ):
            return False
        return True
        