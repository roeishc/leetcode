class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        cache = {}

        def traverse(r, c, previous_value, moves):
            if r == -1 or r == rows or c == cols or grid[r][c] <= previous_value:
                return moves - 1    # remove 1 for stepping out of bounds
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] =  max(
                traverse(r + 1, c + 1, grid[r][c], moves + 1),
                traverse(r, c + 1, grid[r][c], moves + 1),
                traverse(r - 1, c + 1, grid[r][c], moves + 1)
            )
            return cache[(r, c)]

        res = 0
        for i in range(rows):
            res = max(res, traverse(i, 0, 0, 0))
            if res == cols - 1: # slight optimization: if maximum moves reached (according to size of grid), return
                return res

        return res
