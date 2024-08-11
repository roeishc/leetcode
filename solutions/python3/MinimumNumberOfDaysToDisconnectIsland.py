class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        num_of_islands, land = self.count_islands(grid)

        # if there are 0 islands or more than 1 island, we don't need to do anything. return 0
        if num_of_islands != 1: # if num_of_islands == 0 or num_of_islands > 1:
            return 0
    
        # if there is one island, we either need to remove exactly 1 land cell, or exactly 2 land cells.
        # there are no other possibilities (that's the trick to this question)

        # check if we can remove just 1 land cell and end up with 2 islands
        for row, col in land:
            grid[row][col] = 0
            islands, _ = self.count_islands(grid)
            if islands != 1:
                return 1
            grid[row][col] = 1

        # if we couldn't find any land cell to remove such that we're left with 2 islands, then the only
        # other possibility is to remove 2 land cells to end up with 2 islands.
        return 2

    
    def count_islands(self, grid: List[List[int]]) -> (int, set):

        def dfs(row, col):
            if (
                row < 0 or col < 0 or 
                row == rows or col == cols or
                grid[row][col] == 0 or
                (row, col) in visited
                ):
                return
            visited.add((row, col))
            neighbors = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
            for nr, nc in neighbors:
                dfs(nr, nc)

        rows, cols = len(grid), len(grid[0])
        num_of_islands = 0
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col)
                    num_of_islands += 1

        return num_of_islands, visited
