class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [[0] * n for _ in range(m)]  # 0 free, 1 guard, 2 wall, 3 guarded

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] # up, right, down, left
        def mark_guarded(r, c):
            for dr, dc in directions:
                cur_r, cur_c = r + dr, c + dc
                while (
                    0 <= cur_r < m and
                    0 <= cur_c < n and
                    grid[cur_r][cur_c] not in [1, 2]    # not a guard or a wall
                ):
                    grid[cur_r][cur_c] = 3
                    cur_r += dr
                    cur_c += dc
            
        for r, c in guards:
            mark_guarded(r, c)

        res = 0

        for row in grid:
            res += row.count(0)
        
        return res
