"""
Third solution: improved the second solution by not using DFS on grid1 at all.
The gist: for each island found in grid2, iterate through its cells, and if they're all
land in grid1 (value == 1), increment the result by 1.
"""
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        grid2_visited = set()
        res = 0

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if (
                    grid1[i][j] == 1 and
                    grid2[i][j] == 1 and
                    (i, j) not in grid2_visited
                ):
                    cur_island = set()
                    self._dfs(i, j, grid2, grid2_visited, cur_island)
                    if self._is_sub_island(cur_island, grid1):
                        res += 1

        return res


    def _is_sub_island(self, cur_island: set, grid1: List[List[int]]) -> bool:
        count, total = 0, len(cur_island)
        for r, c in cur_island:
            if grid1[r][c] == 1:
                count += 1
        return count == total


    def _dfs(self, start_row: int, start_col: int, grid: List[List[int]], visited: set, island: set):
        
        visited.add((start_row, start_col))
        island.add((start_row, start_col))
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for direction in directions:
            move = (start_row + direction[0], start_col + direction[1])
            if (
                move[0] >= 0 and move[1] >= 0 and
                move[0] < len(grid) and move[1] < len(grid[0]) and
                move not in visited and
                grid[move[0]][move[1]] == 1
            ):
                visited.add(move)
                island.add(move)
                self._dfs(move[0], move[1], grid, visited, island)



"""
Second solution worked, but slow.
For each "candidate" cell (is 1 in both grid1 and grid2), find its island in both grid1 and grid2, and check if
its grid2-island is a subset of its grid1-island.
"""
# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

#         grid2_visited = set()
#         grid1_cell_to_island = {}   # map cells to their matching islands in grid1
#         res = 0

#         for i in range(len(grid1)):
#             for j in range(len(grid1[0])):
#                 if (    # can be a sub-island iff both are land, and it's a "new island" in grid2 (we haven't visited it yet)
#                     grid1[i][j] == 1 and
#                     grid2[i][j] == 1 and
#                     (i, j) not in grid2_visited
#                 ):
#                     if (i, j) not in grid1_cell_to_island:  # if it's a land cell we haven't been to yet in grid1
#                         grid1_visited = set()
#                         cur_island1 = set()
#                         self._dfs(i, j, grid1, grid1_visited, cur_island1)
                        
#                         # map all cells to this island (caching)
#                         frozen_cur_island1 = frozenset(cur_island1)
#                         for cell in cur_island1:
#                             if cell not in grid1_cell_to_island:
#                                 grid1_cell_to_island[cell] = frozen_cur_island1
#                     else:
#                         cur_island1 = grid1_cell_to_island[(i, j)]

#                     cur_island2 = set()
#                     self._dfs(i, j, grid2, grid2_visited, cur_island2)
                    
#                     if cur_island2.issubset(cur_island1):
#                         res += 1

#         return res


#     def _dfs(self, start_row: int, start_col: int, grid: List[List[int]], visited: set, island: set):
        
#         visited.add((start_row, start_col))
#         island.add((start_row, start_col))
        
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
#         for direction in directions:
#             move = (start_row + direction[0], start_col + direction[1])
#             if (
#                 move[0] >= 0 and move[1] >= 0 and
#                 move[0] < len(grid) and move[1] < len(grid[0]) and
#                 move not in visited and
#                 grid[move[0]][move[1]] == 1
#             ):
#                 visited.add(move)
#                 island.add(move)
#                 self._dfs(move[0], move[1], grid, visited, island)
     


"""
Initial solution resulted in time limit exceeded.
I tried finding all islands of grid1, then finding all islands of grid2, and then for each cell,
if it has an island in grid2, check if it's a sub-island of an island in grid1.
"""
# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

#         grid1_visited = set()
#         grid1_islands = set()
#         for i in range(len(grid1)):
#             for j in range(len(grid1[0])):
#                 if grid1[i][j] == 1 and (i, j) not in grid1_visited:
#                     cur_island = set()
#                     self._dfs(i, j, grid1, grid1_visited, cur_island)
#                     grid1_islands.add(frozenset(cur_island))
        
#         grid2_visited = set()
#         grid2_islands = set()
#         for i in range(len(grid2)):
#             for j in range(len(grid2[0])):
#                 if grid2[i][j] == 1 and (i, j) not in grid2_visited:
#                     cur_island = set()
#                     self._dfs(i, j, grid2, grid2_visited, cur_island)
#                     grid2_islands.add(frozenset(cur_island))

#         grid1_cell_to_island = {}
#         for island in grid1_islands:
#             for cell in island:
#                 grid1_cell_to_island[cell] = island
#         grid2_cell_to_island = {}
#         for island in grid2_islands:
#             for cell in island:
#                 grid2_cell_to_island[cell] = island
        
#         res = 0

#         verified_islands = set()
#         for i in range(len(grid1)):
#             for j in range(len(grid1[0])):
#                 if (
#                     grid1[i][j] == 1 and
#                     grid2[i][j] == 1 and
#                     grid2_cell_to_island[(i, j)] not in verified_islands and
#                     grid2_cell_to_island[(i, j)].issubset(grid1_cell_to_island[(i, j)])
#                 ):
#                     verified_islands.add(grid2_cell_to_island[(i, j)])
#                     res += 1
        
#         return res


#     def _dfs(self, start_row: int, start_col: int, grid: List[List[int]], visited: set, island: set):
        
#         visited.add((start_row, start_col))
#         island.add((start_row, start_col))
        
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
#         for direction in directions:
#             move = (start_row + direction[0], start_col + direction[1])
#             if (
#                 move[0] >= 0 and move[1] >= 0 and
#                 move[0] < len(grid) and move[1] < len(grid[0]) and
#                 move not in visited and
#                 grid[move[0]][move[1]] == 1
#             ):
#                 visited.add(move)
#                 island.add(move)
#                 self._dfs(move[0], move[1], grid, visited, island)
        