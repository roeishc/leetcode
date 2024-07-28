class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    self._bfs(grid, rows, cols, visit, r, c)
                    islands += 1
        
        return islands


    def _bfs(self, grid: List[List[int]], rows: int, cols: int, visit: set, r: int, c: int):
        
        #             right   left     up      down
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        q = deque([(r, c)])
        visit.add((r, c))

        while q:
            cur_row, cur_col = q.popleft()
            for vert, horz in directions:
                step_vert, step_horz = cur_row + vert, cur_col + horz
                if (
                    0 <= step_vert < rows and
                    0 <= step_horz < cols and
                    (step_vert, step_horz) not in visit and
                    grid[step_vert][step_horz] == "1"
                ):
                    q.append((step_vert, step_horz))
                    visit.add((step_vert, step_horz))
