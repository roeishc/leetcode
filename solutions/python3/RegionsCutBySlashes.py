class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        ROWS1, COLS1 = len(grid), len(grid[0])
        ROWS2, COLS2 = 3 * ROWS1, 3 * COLS1
        grid2 = [[0] * COLS2 for _ in range(ROWS2)]

        for r1 in range(ROWS1):
            for c1 in range(COLS1):
                r2, c2 = r1 * 3, c1 * 3
                if grid[r1][c1] == "/":
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[r1][c1] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited):
            if (
                r < 0 or c < 0 or
                r == ROWS2 or c == COLS2 or
                grid2[r][c] == 1 or
                (r, c) in visited
                ):
                return
            visited.add((r, c))
            for nei in neighbors:
                dfs(r + nei[0], c + nei[1], visited)
        
        visited = set()
        res = 0
        for r in range(ROWS2):
            for c in range(COLS2):
                if grid2[r][c] == 0 and (r, c) not in visited:
                    dfs(r, c, visited)
                    res += 1
        return res
